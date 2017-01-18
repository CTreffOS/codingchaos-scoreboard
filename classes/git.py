#import oauth2 as oauth
import urllib.request as urllib2
import json
import base64

class git_servant:
    def __init__(self, config):
        self.__username = config.get('codingchaos', 'username')
        self.__password = config.get('codingchaos', 'password')
        self.__tmp_dir = config.get('codingchaos', 'tmp_dir')
        self.__root_repository = config.get('codingchaos', 'root_repository')
        self.__repository_api_url = self.makeApiURL(self.__root_repository)


        # Hier gebe ich auf
        # More to read here: https://developer.github.com/v3/oauth_authorizations/#create-a-new-authorization
        req = urllib2.Request("https://api.github.com/authorizations")
        passwUsername = self.__username + ':' + self.__password
        passwUsername = passwUsername.replace('\n', '')
        base64string = base64.b64encode(passwUsername.encode('utf-8'))
        req.add_header("Authorization", "Basic %s" % base64string)
        data = bytes(json.dumps({"scopes":["repo"], "note":"Access to your repository."}).encode('utf-8'))
        result = urllib2.urlopen(req, data)
        #result = json.loads('\n'.join(result.readlines()))


        '''
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, "https://api.github.com/", self.__username, self.__password)
        urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))

        req = urllib2.Request("https://api.github.com/authorizations")
        data = bytes(json.dumps({"scopes":["public_repo"], "note":"Access to your repository."}).encode('utf-8'))
        f = urllib2.urlopen(req, data)
        result = f.read()
        '''
        self.__token = result['token']

        f_json = self.__makeAPICall(self.__repository_api_url, '/forks')

        self.__fork_urls = []
        for fork in f_json:
            self.__fork_urls.append(fork['url'])
        self.print_self()

    def print_self(self):
        print('Username: '+ self.__username)
        print('Password: '+ self.__password)
        print('Temp Dir: ' + self.__tmp_dir)
        print('Root Repo: ' + self.__root_repository)
        print('API Root: ' + self.__repository_api_url)
        i = 0
        for url in self.__fork_urls:
            if i == 0:
                print('Fork URLS: ' + url)
            else:
                print('           ' + url)
            i = i + 1

    def makeApiURL(self, url):
        apiURL = self.__root_repository[0:url.find('github')] +\
                                        'api.' + \
                                        url[url.find('github'): \
                                        url.find('github.com/')+ len('github.com/')] + \
                                        'repos/' + \
                                        url[url.find('github.com/')+ len('github.com/'): \
                                        len(url)]
        return apiURL

    def __makeAPICall(self, url, call):
        '''
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None,
                             "https://api.github.com/",
                             self.__username,
                             self.__password)
        urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))
        print('About to call: ' + url +  call)
        try:
            req = urllib2.Request(url + call)
            f = urllib2.urlopen(req)
            f_json = json.loads(f.read().decode('utf-8'))
            return f_json
        except Exception:
            import traceback
            print(traceback.format_exc())
            return None
        '''
        print('About to call: ' + url +  call)

        try:
            req = urllib2.Request(url + call)
            req.add_header("Authorization", "token %s" % self.__token)
            result = urllib2.urlopen(req)
            f_json = json.loads(result.read().decode('utf-8'))
            return f_json
        except Exception:
            import traceback
            print(traceback.format_exc())
            return None

    def getAufgabeMaster(self, aufgabe):
        f_json = self.__makeAPICall(self.__fork_urls[1], '/commits?path='+aufgabe)
        print(f_json)
        for commit in f_json:
            #print(commit)
            date = commit['commit']['author']['date']
            print("Date of commit: " + date)
            tree_url = commit['commit']['tree']['url']
            print(tree_url)
            t_json = self.__makeAPICall(tree_url, '')
            print(t_json)
    '''
        f_json = self.__makeAPICall(self.__fork_urls[1], 'contents/' + aufgabe)
        if f_json is None:
            return None
        #print(f_json[0])
        f_json = self.__makeAPICall(self.__fork_urls[1], 'aufgabe00/commits')
        print(f_json)
    '''