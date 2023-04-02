# 221RDB231 Emīlija Ostaševska 4.gr


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    contacts = {}
    result = []

    for current_query in queries:
        if current_query.type == 'add':
            contacts[current_query.number] = current_query.name
        elif current_query.type == 'del' and current_query.number in contacts:
            del contacts[current_query.number]
        elif current_query.type == 'find':
            response = 'not found'
            if current_query.number in contacts:
                response = contacts[current_query.number]
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))