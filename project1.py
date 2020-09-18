movies = []
def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie ,and 'q' stopping:")

    while user_input !='q':
        if user_input =='a':
            add_movie()
        elif user_input == 'l':
            show_movie()
        elif user_input =='f':
            find_movie()
        else:
            print('Unknown command-please try agin.')

        user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie ,and 'q' stopping:")


def add_movie():
    name = input('Name of movie:')
    director = input('Name of director of movie:')
    year = input('Which year movie was released:')

    movies.append({
        'name':name,
        'director': director,
        'year': year
    })

def show_movie():
    for movie in movies:
        print(f"name: {movie['name']}")
        print(f"director: {movie['director']}")
        print(f"year: {movie['year']}")

def find_movie():
    find_by = input("what property of movie are you looking for? :")
    looking_for = input("what are you searching for? :")

    found_movies = find_by_attribute(movies, looking_for,lambda x:x[find_by])
    show_movie(found_movies,)

def find_by_attribute(items, expected,finder):
    found =[]
    for i in items:
        if finder(i) == expected:
            found.append(i)
        return found
menu()
