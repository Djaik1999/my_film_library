import json
import re
import time


start_time = time.time()

road_to_file = "films/watched.txt"

date_row_check = str.maketrans("", "", ".: ")

films = list()
counter = 1
with open(road_to_file, "r", encoding="utf_8_sig") as file:
    film = dict()
    for row in file:

        # Строка с датой
        if row[:13].translate(date_row_check).isnumeric():

            # ID
            film["id"] = counter
            counter += 1

            # Can be comment in date row, check for this
            check_for_comments = [el.strip() for el in row.split("\t") if el.strip()]
            if len(check_for_comments) > 1:
                comments_in_date_row = check_for_comments[1:]
                # Exist check
                if "Comments" in film:                    
                    film["Comments"].append(comments_in_date_row)
                    film["Watched"] = check_for_comments[0]
                else:
                    film["Comments"] = [comments_in_date_row[0].strip()]
            else:
                film["Watched"] = row.strip()

            films.append(film)
            
            # For new film, this film done
            film = dict()

        # Строка содержащая название, год выхода, мою оценку, комментарии (в которые включены и актёры)
        else:
            splitted_row = [el.strip() for el in row.split("\t") if el.strip()]

            # Ver 1: Потеряла актуальность, можно удалять

            # Title
            # try:
            #     film["Title"] = splitted_row[0]
            # except:
            #     film["Title"] = ""
            #     print(row)

            # # Comments
            # try:
            #     film["Comments"] = splitted_row[3]

            #     comments = re.split(r"(?<!\()\s*\+\s*(?!\))", splitted_row[3])

            #     # print(comments)
            #     # if comments:
            #     #     for comment in comments:
            #     #         # print(comment.strip())
            # except Exception as ex:
            #     film["Comments"] = ""

            # # Grade
            # try:
            #     film["Grade"] = splitted_row[2]
            # except Exception as ex:
            #     film["Grade"] = ""

            # # Year
            # try:
            #     film["Year"] = splitted_row[1]
            # except Exception as ex:
            #     film["Year"] = ""

            
            # Ver 2

            indexes = len(splitted_row)

            index_dict = {
                0 : "Title",
                1: "Year",
                2: "Grade",
                3: "Comments",
            }

            for i in range(0, indexes):
                try:
                    # Разбиваем комментарии по + который не находится внутри ()
                    if index_dict[i] == "Comments":
                        comments = re.split(r"(?<!\()\s*\+\s*(?!\))", splitted_row[i])
                        
                        # Ищем имена актёров в коментариях (2 анг слова с большой буквы)
                        for comment in comments:
                            if re.match(r"([A-Z][a-z]*)\s([A-Z][a-z]*)(.*)", comment):
                                if "Cast" not in film:
                                    film["Cast"] = list()

                                film["Cast"].append(comment)                        

                        # Если удаляю в верхнем цикле, то смещаются индексы и не все записывается, поэтому удаляю здесь
                        if "Cast" in film:
                            for actor in film["Cast"]:
                                # Удаляем из комментариев
                                comments.remove(actor)

                        film[index_dict[i]] = comments
                    else:
                        film[index_dict[i]] = splitted_row[i]
                except Exception as ex:
                    # For DEBUG
                    print(splitted_row)
                    print(ex)
                    raise ex
                

with open("films/watched.json", "w", encoding="utf_8_sig") as file:
    json.dump(films, file, indent=4, ensure_ascii=False)


end_time = time.time() - start_time
print(f"{end_time} sec.")