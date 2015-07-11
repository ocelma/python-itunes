__author__ = 'tal'
def makePrecise(query,results):
    '''
    :param query: the query searched for
    :param results: the result set returned by the itunes api
    :return:results that are an exact match
    '''
    f =filter(lambda x: x.name==query,results)
    return [res for res in f]

def filterOn(key,val,results,case_insensitive=False,substring=False):
    '''
    Allows filtering of itunes results by a second field. (Can be applied multiple times)
    Useful when your retreive a track by name and want to filter by artist
    :param key: The key you want to filter by
    :param val: The value that key should be
    :param results: The results set returned by itunes
    :param case_insensitive: Case insensitive filter
    :param substring: if True, check if the value is a substring of the field
    :return:The filtered result set
    '''
    lower = (lambda x: x.lower()) if case_insensitive is True else (lambda x: x)
    match = (lambda x,y: x in y) if substring is True else (lambda x,y: x==y)
    val = lower(val)
    print (val)
    f =filter(lambda x: match(val,lower(x.__getattribute__(key).name)),results)
    return [res for res in f]