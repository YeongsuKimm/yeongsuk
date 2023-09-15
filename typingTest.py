import random, time, random_word
test_data = {
    0 : "The sun was setting behind the distant mountains, casting a warm, golden glow across the tranquil valley below. Birds chirped their evening songs, and a gentle breeze rustled through the leaves of the trees that lined the peaceful riverbank. As the day drew to a close, the world seemed to sigh in contentment, embracing the serenity of twilight.",
    1 : "In the heart of the bustling city, the streets were alive with activity. People hurried along the crowded sidewalks, their footsteps echoing off the tall buildings that surrounded them. Car horns honked, and sirens wailed in the distance, creating a cacophony of urban sounds. Despite the chaos, there was an energy and vibrancy that defined city life, a rhythm that never seemed to falter.",
    2 : "The ancient castle stood atop a steep hill, its weathered stone walls bearing witness to centuries of history. Ivy clung to the fortress's facade, and the drawbridge creaked as it lowered, revealing a hidden world of intrigue and mystery. Within the castle's grand halls, portraits of long-deceased royalty gazed down, their eyes seeming to follow your every move.",
    3 : "Amid the sprawling savanna, the majestic lions roamed freely, their powerful muscles rippling beneath golden fur. The sun beat down relentlessly, creating shimmering waves of heat across the vast expanse. Nearby, a herd of graceful gazelles grazed, their delicate movements a stark contrast to the raw strength of the predators. In this untamed wilderness, the circle of life played out in a never-ending drama.",
    4 : "In the heart of the tempest, lightning streaked across the obsidian sky, illuminating the turbulent clouds that swirled menacingly overhead. Thunder rumbled like an angry giant's roar, shaking the very earth beneath your feet. Rain poured in relentless sheets, soaking everything in its path. It was a moment of raw, untamed nature, a reminder of the awesome power of the elements.",
    5 : "Within the labyrinthine catacombs, ancient secrets lay hidden beneath layers of forgotten history. Torches sputtered, casting eerie shadows on the cold, damp walls, as you navigated the winding passages, each one seemingly more treacherous than the last. The air was thick with the scent of age-old dust and decay, and the distant echoes of dripping water added to the eerie atmosphere. It was a journey into the unknown, a quest for knowledge buried deep in the earth.",
    6 : "Beneath the star-studded canopy of the night sky, a meteor shower erupted, filling the heavens with a dazzling display of celestial fireworks. Each streak of light marked the end of a cosmic journey spanning eons. It was a reminder of the vastness of the universe, where time and space merged into a breathtaking spectacle.",
    7 : "In the laboratory of the brilliant scientist, intricate machines hummed with purpose, their gears and circuits working in harmonious precision. Beakers bubbled with mysterious concoctions, and charts covered the walls, revealing the complexities of groundbreaking research. The scientist's mind was a whirlwind of ideas, seeking to unlock the secrets of the universe. It was a world where innovation and discovery danced on the edge of the unknown.",
    # 8 : "", 
    # 9 : "",
    # 10 : "",
    # 11 : "",
    # 12 : "",
    # 13 : "",
    # 14 : "",
    # 15 : "",
    # 16 : "",
    # 17 : "",
    # 18 : "",
    # 19 : "",
    # 20 : "",
}

def test1():
    rand = random.randint(0,len(test_data)+1);
    input("Press enter when you want to start\n >")
    print(test_data[rand]);
    start = time.perf_counter();
    words = input("TYPE:")
    end = time.perf_counter();
    totalTime = end - start;
    print("Completed in " + str(totalTime) + " seconds");
    print(words);
    total = 0;
    words = words.split();
    data = test_data[rand].split();
    all = 0;
    if(len(data) > len(words)):
        for i in range(len(words)):
            if data[i] == words[i]:
                total+=1;
            all += 1;
    else:
        for i in range(len(data)):
            if data[i] == words[i]:
                total+=1;
            all += 1;
    print("WPM: " + str(total/(totalTime)*60));
    try: 
        print("Accuracy: " + str(total/all*100)+ "%")
    except:
        pass;
def test2():
    words = [];
    all = 0;
    try:   
        length = int(input("Enter number of words: "))
    except:
        print("Invalid type")
        return;
    r = random_word.RandomWords();
    for i in range(length):
        words.append(r.get_random_word);
        print(r.get_random_word)
    input("\nPress enter when you want to start\n >")
    total = 0;
    start = time.perf_counter();
    # sentence = " ".join(words)
    print(words)
    result = input("TYPE:")
    end = time.perf_counter();
    totalTime = end - start;
    print("Completed in " + str(totalTime) + " seconds");
    if(len(words) > len(result)):
        for i in range(len(result)):
            if words[i] == result[i]:
                total+=1;
            all += 1;
    else:
        for i in range(len(words)):
            if words[i] == result[i]:
                total+=1;
            all += 1;
    try: 
        print("Accuracy: " + str(total/all*100)+ "%")
    except:
        pass;
    
test2();
# x = ["1", "2", "3", "4"]
# print(" ".join(x))