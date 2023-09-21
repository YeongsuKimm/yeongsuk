
import random, time, random_word, unittest, sys, io
from unittest.mock import patch
from io import StringIO
test_data = {
    0 : "The sun was setting behind the distant mountains, casting a warm, golden glow across the tranquil valley below. Birds chirped their evening songs, and a gentle breeze rustled through the leaves of the trees that lined the peaceful riverbank. As the day drew to a close, the world seemed to sigh in contentment, embracing the serenity of twilight.",
    1 : "In the heart of the bustling city, the streets were alive with activity. People hurried along the crowded sidewalks, their footsteps echoing off the tall buildings that surrounded them. Car horns honked, and sirens wailed in the distance, creating a cacophony of urban sounds. Despite the chaos, there was an energy and vibrancy that defined city life, a rhythm that never seemed to falter.",
    2 : "The ancient castle stood atop a steep hill, its weathered stone walls bearing witness to centuries of history. Ivy clung to the fortress's facade, and the drawbridge creaked as it lowered, revealing a hidden world of intrigue and mystery. Within the castle's grand halls, portraits of long-deceased royalty gazed down, their eyes seeming to follow your every move.",
    3 : "Amid the sprawling savanna, the majestic lions roamed freely, their powerful muscles rippling beneath golden fur. The sun beat down relentlessly, creating shimmering waves of heat across the vast expanse. Nearby, a herd of graceful gazelles grazed, their delicate movements a stark contrast to the raw strength of the predators. In this untamed wilderness, the circle of life played out in a never-ending drama.",
    4 : "In the heart of the tempest, lightning streaked across the obsidian sky, illuminating the turbulent clouds that swirled menacingly overhead. Thunder rumbled like an angry giant's roar, shaking the very earth beneath your feet. Rain poured in relentless sheets, soaking everything in its path. It was a moment of raw, untamed nature, a reminder of the awesome power of the elements.",
    5 : "Within the labyrinthine catacombs, ancient secrets lay hidden beneath layers of forgotten history. Torches sputtered, casting eerie shadows on the cold, damp walls, as you navigated the winding passages, each one seemingly more treacherous than the last. The air was thick with the scent of age-old dust and decay, and the distant echoes of dripping water added to the eerie atmosphere. It was a journey into the unknown, a quest for knowledge buried deep in the earth.",
    6 : "Beneath the star-studded canopy of the night sky, a meteor shower erupted, filling the heavens with a dazzling display of celestial fireworks. Each streak of light marked the end of a cosmic journey spanning eons. It was a reminder of the vastness of the universe, where time and space merged into a breathtaking spectacle.",
    7 : "In the laboratory of the brilliant scientist, intricate machines hummed with purpose, their gears and circuits working in harmonious precision. Beakers bubbled with mysterious concoctions, and charts covered the walls, revealing the complexities of groundbreaking research. The scientist's mind was a whirlwind of ideas, seeking to unlock the secrets of the universe. It was a world where innovation and discovery danced on the edge of the unknown.",
    8 : "Nestled deep within the heart of the enchanted forest, where ancient trees stood tall and the air was thick with the scent of earth and moss, a hidden glen revealed itself. Here, the sunlight filtered through the canopy in dappled patterns, creating an ethereal ambiance. A gentle stream meandered through the glen, its crystal-clear waters bubbling over smooth stones. Birds sang melodious songs from the branches above, and the tranquility of this secluded paradise offered respite from the chaos of the outside world. It was a place where time seemed to stand still, inviting those who discovered it to pause, reflect, and reconnect with nature.", 
    9 : "In the heart of the bustling city, where skyscrapers touched the sky and traffic moved in a never-ending flow, life was a constant rush. People hurried from one place to another, their faces buried in smartphones, and the streets echoed with the cacophony of car horns and chatter. Amidst this urban chaos, a small park provided a moment of respite. With its greenery and serene pond, it was a sanctuary where city dwellers sought solace from the daily hustle and bustle.",
    10 : "On the edge of town, a quaint bookstore stood with shelves lined with books of all genres. The scent of aged paper and ink filled the air, inviting visitors to explore the world of words within. The owner, a bibliophile, greeted each customer with a warm smile, eager to share the joy of literature. It was a place where stories came to life, and imagination knew no bounds.",
    11 : "The sun dipped below the horizon, casting a warm, orange glow across the horizon. The evening breeze rustled the leaves of the trees, creating a soothing melody. As darkness fell, the stars began to twinkle in the night sky, illuminating the world with their celestial light. It was a peaceful moment, a reminder of the beauty that could be found in the simple act of watching the world transition from day to night.",
    12 : "In a quaint coastal town, where the salty breeze carried the scent of the sea, a seafood restaurant nestled by the waterfront. The aroma of freshly grilled fish and the sound of seagulls filled the air. Diners sat at tables with white tablecloths, savoring the flavors of the ocean while the waves lapped gently against the shore. It was a place where culinary delights and nature's beauty merged, creating a memorable dining experience.",
    13 : "In the heart of the historic district, cobblestone streets wound their way past centuries-old buildings, each with a story to tell. The architecture ranged from Gothic spires to quaint Tudor-style homes, creating a picturesque tableau of bygone eras. Tourists wandered through the narrow alleys, guided by the echoes of history that whispered from the worn stone walls.",
    14 : "In the heart of the ancient forest, where sunlight filtered through the dense canopy of leaves, a tranquil glade opened up. This hidden oasis was a sanctuary for countless species of flora and fauna, all coexisting in a delicate balance. The babbling brook that wound its way through the glade provided a source of life for the creatures that called this place home. The hushed whispers of the wind in the treetops and the songs of the birds created a symphony of nature's own making, a melody that had played out for centuries, undisturbed by the rapid pace of the outside world.",
    15 : "High atop the jagged cliffs that overlooked the turbulent sea, a solitary lighthouse stood as a sentinel against the forces of nature. Its bright beacon pierced the darkness of the night, guiding ships safely through treacherous waters. The lighthouse keeper, a solitary figure in this remote outpost, tended to the light with unwavering dedication, knowing that the safety of countless sailors depended on it. From this vantage point, the vast expanse of the ocean stretched endlessly, a reminder of the boundless power and mystery of the sea.",
    17 : "As the sun dipped below the horizon, casting a warm, golden glow across the tranquil countryside, the small village came to life. Children played in the meadows, their laughter carrying on the breeze, while farmers returned from their fields, their faces etched with the weariness of a day's labor. In the heart of the village, the old town square bustled with activity as market stalls were set up, and the savory aroma of street food wafted through the air. The village, with its cobblestone streets and centuries-old cottages, exuded a timeless charm, a place where tradition and modernity coexisted harmoniously.",
    18 : "Deep in the heart of the enchanted forest, where ancient oaks stood tall and the air was thick with the scent of moss, a hidden glade beckoned. Sunlight filtered through the canopy, casting a dappled tapestry of light and shadow. A gentle stream meandered through the glade, its crystal-clear waters bubbling over smooth stones. Birds sang melodious songs from the branches above, creating an orchestra of nature's own design.",
    19 : "Perched on a rocky promontory overlooking the vast expanse of the ocean, a centuries-old lighthouse stood as a silent sentinel. Its stark white walls and red roof contrasted with the deep blue of the sea and sky. Inside, the spiral staircase wound its way to the top, where the keeper tended to the beacon, ensuring that ships found their way safely through the treacherous waters below.",
    20 : "As the golden hues of autumn leaves fell gently to the ground, the town square transformed into a canvas of vibrant colors. Families gathered to celebrate the harvest festival, with stalls offering apple cider, pumpkin pies, and the sweet aroma of caramel apples. Children played games, their laughter mingling with the live folk music that filled the air, creating a joyful atmosphere.",
}
def test1(tindex = -1):
    if(tindex == -1):
        index = random.randint(0,len(test_data)-1)
    else:
        index = tindex;
    print(test_data[index]);
    start = time.perf_counter();
    words = input("TYPE:")
    end = time.perf_counter();
    totalTime = end - start;
    print(f"Completed in {str(totalTime)} seconds");
    total = 0;
    words = words.split();
    data = test_data[index].split();
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
    try: 
        accuracy = f"{str(total / all * 100)}%";
    except ZeroDivisionError:
        accuracy = "0.0%";
    try:
        wpm = str(total / totalTime * 60);
    except ZeroDivisionError:
        wpm = "0.0";
    print(f"Accuracy: {accuracy}");
    print(f"WPM: {wpm}");
    return accuracy;
class TestCases(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["The sun was setting behind the distant mountains, casting a warm, golden glow across the tranquil valley below. Birds chirped their evening songs, and a gentle breeze rustled through the leaves of the trees that lined the peaceful riverbank. As the day drew to a close, the world seemed to sigh in contentment, embracing the serenity of twilight."])
    def test_case1(self, mock_input):
        result = test1(0)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["In the heart of the bustling city, the streets were alive with activity. People hurried along the crowded sidewalks, their footsteps echoing off the tall buildings that surrounded them. Car horns honked, and sirens wailed in the distance, creating a cacophony of urban sounds. Despite the chaos, there was an energy and vibrancy that defined city life, a rhythm that never seemed to falter."])
    def test_case2(self, mock_input):
        result = test1(1)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["The ancient castle stood atop a steep hill, its weathered stone walls bearing witness to centuries of history. Ivy clung to the fortress's facade, and the drawbridge creaked as it lowered, revealing a hidden world of intrigue and mystery. Within the castle's grand halls, portraits of long-deceased royalty gazed down, their eyes seeming to follow your every move."])
    def test_case3(self, mock_input):
        result = test1(2)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";
    # ... (previous test cases)

    @patch('builtins.input', side_effect=["Amid the sprawling savanna, the majestic lions roamed freely, their powerful muscles rippling beneath golden fur. The sun beat down relentlessly, creating shimmering waves of heat across the vast expanse. Nearby, a herd of graceful gazelles grazed, their delicate movements a stark contrast to the raw strength of the predators. In this untamed wilderness, the circle of life played out in a never-ending drama."])
    def test_case4(self, mock_input):
        result = test1(3)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["In the heart of the tempest, lightning streaked across the obsidian sky, illuminating the turbulent clouds that swirled menacingly overhead. Thunder rumbled like an angry giant's roar, shaking the very earth beneath your feet. Rain poured in relentless sheets, soaking everything in its path. It was a moment of raw, untamed nature, a reminder of the awesome power of the elements."])
    def test_case5(self, mock_input):
        result = test1(4)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["Within the labyrinthine catacombs, ancient secrets lay hidden beneath layers of forgotten history. Torches sputtered, casting eerie shadows on the cold, damp walls, as you navigated the winding passages, each one seemingly more treacherous than the last. The air was thick with the scent of age-old dust and decay, and the distant echoes of dripping water added to the eerie atmosphere. It was a journey into the unknown, a quest for knowledge buried deep in the earth."])
    def test_case6(self, mock_input):
        result = test1(5)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["Beneath the star-studded canopy of the night sky, a meteor shower erupted, filling the heavens with a dazzling display of celestial fireworks. Each streak of light marked the end of a cosmic journey spanning eons. It was a reminder of the vastness of the universe, where time and space merged into a breathtaking spectacle."])
    def test_case7(self, mock_input):
        result = test1(6)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["In the laboratory of the brilliant scientist, intricate machines hummed with purpose, their gears and circuits working in harmonious precision. Beakers bubbled with mysterious concoctions, and charts covered the walls, revealing the complexities of groundbreaking research. The scientist's mind was a whirlwind of ideas, seeking to unlock the secrets of the universe. It was a world where innovation and discovery danced on the edge of the unknown."])
    def test_case8(self, mock_input):
        result = test1(7)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["Nestled deep within the heart of the enchanted forest, where ancient trees stood tall and the air was thick with the scent of earth and moss, a hidden glen revealed itself. Here, the sunlight filtered through the canopy in dappled patterns, creating an ethereal ambiance. A gentle stream meandered through the glen, its crystal-clear waters bubbling over smooth stones. Birds sang melodious songs from the branches above, and the tranquility of this secluded paradise offered respite from the chaos of the outside world. It was a place where time seemed to stand still, inviting those who discovered it to pause, reflect, and reconnect with nature."])
    def test_case9(self, mock_input):
        result = test1(8)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["In the heart of the bustling city, where skyscrapers touched the sky and traffic moved in a never-ending flow, life was a constant rush. People hurried from one place to another, their faces buried in smartphones, and the streets echoed with the cacophony of car horns and chatter. Amidst this urban chaos, a small park provided a moment of respite. With its greenery and serene pond, it was a sanctuary where city dwellers sought solace from the daily hustle and bustle."])
    def test_case10(self, mock_input):
        result = test1(9)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";
        
    @patch('builtins.input', side_effect=["On the edge of town, a quaint bookstore stood with shelves lined with books of all genres. The scent of aged paper and ink filled the air, inviting visitors to explore the world of words within. The owner, a bibliophile, greeted each customer with a warm smile, eager to share the joy of literature. It was a place where stories came to life, and imagination knew no bounds."])
    def test_case11(self, mock_input):
        result = test1(10)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["The sun dipped below the horizon, casting a warm, orange glow across the horizon. The evening breeze rustled the leaves of the trees, creating a soothing melody. As darkness fell, the stars began to twinkle in the night sky, illuminating the world with their celestial light. It was a peaceful moment, a reminder of the beauty that could be found in the simple act of watching the world transition from day to night."])
    def test_case12(self, mock_input):
        result = test1(11)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["In a quaint coastal town, where the salty breeze carried the scent of the sea, a seafood restaurant nestled by the waterfront. The aroma of freshly grilled fish and the sound of seagulls filled the air. Diners sat at tables with white tablecloths, savoring the flavors of the ocean while the waves lapped gently against the shore. It was a place where culinary delights and nature's beauty merged, creating a memorable dining experience."])
    def test_case13(self, mock_input):
        result = test1(12)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["In the heart of the historic district, cobblestone streets wound their way past centuries-old buildings, each with a story to tell. The architecture ranged from Gothic spires to quaint Tudor-style homes, creating a picturesque tableau of bygone eras. Tourists wandered through the narrow alleys, guided by the echoes of history that whispered from the worn stone walls."])
    def test_case14(self, mock_input):
        result = test1(13)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["In the heart of the ancient forest, where sunlight filtered through the dense canopy of leaves, a tranquil glade opened up. This hidden oasis was a sanctuary for countless species of flora and fauna, all coexisting in a delicate balance. The babbling brook that wound its way through the glade provided a source of life for the creatures that called this place home. The hushed whispers of the wind in the treetops and the songs of the birds created a symphony of nature's own making, a melody that had played out for centuries, undisturbed by the rapid pace of the outside world."])
    def test_case15(self, mock_input):
        result = test1(14)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["High atop the jagged cliffs that overlooked the turbulent sea, a solitary lighthouse stood as a sentinel against the forces of nature. Its bright beacon pierced the darkness of the night, guiding ships safely through treacherous waters. The lighthouse keeper, a solitary figure in this remote outpost, tended to the light with unwavering dedication, knowing that the safety of countless sailors depended on it. From this vantage point, the vast expanse of the ocean stretched endlessly, a reminder of the boundless power and mystery of the sea."])
    def test_case16(self, mock_input):
        result = test1(15)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["As the sun dipped below the horizon, casting a warm, golden glow across the tranquil countryside, the small village came to life. Children played in the meadows, their laughter carrying on the breeze, while farmers returned from their fields, their faces etched with the weariness of a day's labor. In the heart of the village, the old town square bustled with activity as market stalls were set up, and the savory aroma of street food wafted through the air. The village, with its cobblestone streets and centuries-old cottages, exuded a timeless charm, a place where tradition and modernity coexisted harmoniously."])
    def test_case17(self, mock_input):
        result = test1(17)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["Deep in the heart of the enchanted forest, where ancient oaks stood tall and the air was thick with the scent of moss, a hidden glade beckoned. Sunlight filtered through the canopy, casting a dappled tapestry of light and shadow. A gentle stream meandered through the glade, its crystal-clear waters bubbling over smooth stones. Birds sang melodious songs from the branches above, creating an orchestra of nature's own design."])
    def test_case18(self, mock_input):
        result = test1(18)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["Perched on a rocky promontory overlooking the vast expanse of the ocean, a centuries-old lighthouse stood as a silent sentinel. Its stark white walls and red roof contrasted with the deep blue of the sea and sky. Inside, the spiral staircase wound its way to the top, where the keeper tended to the beacon, ensuring that ships found their way safely through the treacherous waters below."])
    def test_case19(self, mock_input):
        result = test1(19)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";

    @patch('builtins.input', side_effect=["As the golden hues of autumn leaves fell gently to the ground, the town square transformed into a canvas of vibrant colors. Families gathered to celebrate the harvest festival, with stalls offering apple cider, pumpkin pies, and the sweet aroma of caramel apples. Children played games, their laughter mingling with the live folk music that filled the air, creating a joyful atmosphere."])
    def test_case20(self, mock_input):
        result = test1(20)
        try:
            self.assertEqual(result, '100.0%')
        except AssertionError:
            return "WRONG";


if __name__ == '__main__':
    unittest.main();   