from abc import ABC, abstractmethod
import requests, json, os


class RequestsClass(ABC):

    def __init__(self, hostname, params=None):
        self.hostname = hostname
        self.params =  params


    def get_request(self, endpoint):
        url = self.hostname + endpoint
        try:
            r = requests.get(url=url, params=self.params)
        except Exception as err:
            print('Error:', err)
        if r.status_code == 200:
            return r.json()
        else:
            print("There was an error procesing your request")


class GetKeys(ABC):
    
    @abstractmethod
    def get_key(self, key):
        return os.getenv(key)


class GetFood(RequestsClass, GetKeys):
    
    def __init__(self):
        super().__init__('https://api.nal.usda.gov/fdc/v1/')   


    def get_macros(self):
        macros = {'protein':203, 'fat':204, 'carbohydrate':205, 'calories':208, 'sugars':269, 'total_trans':605, 'total_saturated':606,}
        return macros


    def get_params(self,key, macros=False):
        self.params = {}
        key = super().get_key(key)
        if key:
            self.params['api_key'] = key
        if macros:
            macros = self.get_macros()
            self.params["nutrients"] = macros.values()
        return self.params


    def verify_endpoint(endpoint):
        endpoint_list = ['/food', '/foods', '/foods/list', '/foods/search', 'json-spec', '/yaml-spec']
        return True if endpoint in endpoint_list else False

    def get_food(self, endpoint, food=None):
        if self.verify_endpoint(endpoint):
            if food:
                self.url = self.hostname + endpoint + food
                super().get_request()
        else:
            print("The endpoint is not valid")