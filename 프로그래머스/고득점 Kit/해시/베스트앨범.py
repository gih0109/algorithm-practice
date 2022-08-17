def solution(genres, plays):
    genres_list = list(set(genres))
    music_list = [[i, 0, []] for i in genres_list] # 장르, 장르 내 재생 수 합, (고유번호, 재생횟수)

    for idx_1 in range(len(genres)):
        for idx_2 in range(len(music_list)):
            if genres[idx_1] == music_list[idx_2][0]:
                music_list[idx_2][1] += plays[idx_1]
                music_list[idx_2][2].append([idx_1, plays[idx_1]])
    # 정렬
    for i in music_list:
        i[2].sort(key= lambda x: x[0])
        i[2].sort(key= lambda x: x[1], reverse= True)
    music_list.sort(key=lambda x: x[1], reverse= True)

    answer = []
    for i in music_list:
        for j in i[2][:2]:
            answer.append(j[0])
    
    return answer

if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))