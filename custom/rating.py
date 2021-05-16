"""
Реализовать рейтинг
"""

rating = [7,5,3,3,2]

while True:
    user_rating = int(input(f'Добавьте рейтинг {rating}: '))
    if not user_rating:
        break
    rating.reverse()
    if user_rating > max(rating):
        rating.append(user_rating)
    else:
        for idx, val in enumerate(rating):
            if user_rating <= val:
                rating.insert(idx, user_rating)
                break
    rating.reverse()

"""
Добавьте рейтинг [7, 5, 3, 3, 2]: 1
Добавьте рейтинг [7, 5, 3, 3, 2, 1]: 5
Добавьте рейтинг [7, 5, 5, 3, 3, 2, 1]: 4
Добавьте рейтинг [7, 5, 5, 4, 3, 3, 2, 1]: 8
Добавьте рейтинг [8, 7, 5, 5, 4, 3, 3, 2, 1]: 0
Process finished with exit code 0
"""
