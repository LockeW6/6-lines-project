import textwrap

# inputs
def get_three_digit(prompt):
    while True:
        s = input(prompt)
        if not s.strip():
            print("Input cannot be blank. Please enter a valid three-digit number!")
            continue
        try:
            num = int(s)
        except ValueError:
            print("Input is not a valid integer. Please enter a valid three-digit number!")
            continue
        if 100 <= num <= 999:
            return num
        else:
            print("Number must be between 100 and 999. Please try again.")

num1 = get_three_digit("Enter the first three-digit number: ")
num2 = get_three_digit("Enter the second three-digit number: ")
num3 = get_three_digit("Enter the third three-digit number: ")

# labels
remainder1 = num1 % 8
remainder2 = num2 % 8
remainder3 = num3 % 6

yin = "————  ————"
yang = "——————————"

def upper(remainder1):
    if remainder1 == 1:
        return f"{yang}\n{yang}\n{yang}"
    elif remainder1 == 2:
        return f"{yin}\n{yang}\n{yang}"
    elif remainder1 == 3:
        return f"{yang}\n{yin}\n{yang}"
    elif remainder1 == 4:
        return f"{yin}\n{yin}\n{yang}"
    elif remainder1 == 5:
        return f"{yang}\n{yang}\n{yin}"
    elif remainder1 == 6:
        return f"{yin}\n{yang}\n{yin}"
    elif remainder1 == 7:
        return f"{yang}\n{yin}\n{yin}"
    elif remainder1 == 8 or remainder1 == 0:
        return f"{yin}\n{yin}\n{yin}"

def lower(remainder2):
    if remainder2 == 1:
        return f"{yang}\n{yang}\n{yang}"
    elif remainder2 == 2:
        return f"{yin}\n{yang}\n{yang}"
    elif remainder2 == 3:
        return f"{yang}\n{yin}\n{yang}"
    elif remainder2 == 4:
        return f"{yin}\n{yin}\n{yang}"
    elif remainder2 == 5:
        return f"{yang}\n{yang}\n{yin}"
    elif remainder2 == 6:
        return f"{yin}\n{yang}\n{yin}"
    elif remainder2 == 7:
        return f"{yang}\n{yin}\n{yin}"
    elif remainder2 == 8 or remainder2 == 0:
        return f"{yin}\n{yin}\n{yin}"

original_upper = upper(remainder1)
original_lower = lower(remainder2)
Original_6_lines = original_upper + "\n" + original_lower
#print("Original 6 lines：")
#print(Original_6_lines)

#exchange line
def change(change, remainder3):
    if remainder3 == 0:
        return change

    lines = change.strip().splitlines() 
    index = len(lines) - remainder3

    if lines[index] == yin:
        lines[index] = yang
    elif lines[index] == yang:
        lines[index] = yin

    return "\n".join(lines) + "\n"

Changed_6_lines = change(Original_6_lines, remainder3)
#print("Changed 6 lines：")
#print(Changed_6_lines)

text_dict = {
    # 乾为天
    f"{yang}\n{yang}\n{yang}\n{yang}\n{yang}\n{yang}": 
    "TEXT：Stay strong, keep learning, and stay determined—by cultivating virtue and perseverance, you will overcome obstacles and achieve great success.",
    #泽天夬
    f"{yin}\n{yang}\n{yang}\n{yang}\n{yang}\n{yang}": 
    "TEXT：Listen to the advice of others with an open mind, do not be reckless, think deeply, and treat people with a gentle attitude.",
    #火天大有
    f"{yang}\n{yin}\n{yang}\n{yang}\n{yang}\n{yang}": 
    "TEXT：The road ahead is full of challenges and setbacks—only by staying focused and diligent can we keep succeeding. Complacency and overconfidence will lead to major failures.",
    #雷天大壮
    f"{yin}\n{yin}\n{yang}\n{yang}\n{yang}\n{yang}": 
    "TEXT：Don't overexert yourself, especially when things are going well—rash actions could backfire. If you're feeling stuck, focus on protecting yourself and preparing for what's next.",
    #风天小畜
    f"{yang}\n{yang}\n{yin}\n{yang}\n{yang}\n{yang}": 
    "TEXT：Things are unpredictable, and arguments may arise, but they will not be resolved quickly. Stay patient and wait for the right moment.",
    #水天需
    f"{yin}\n{yang}\n{yin}\n{yang}\n{yang}\n{yang}": 
    "TEXT：A wise person must act at the right time. Rushing ahead recklessly will only lead to danger.",
    #山天大畜
    f"{yang}\n{yin}\n{yin}\n{yang}\n{yang}\n{yang}": 
    "TEXT：Do not aim too high and ignore reality; it is better to stay grounded and work steadily. This way, you can achieve great success, but arrogance and disregard for others will only lead to failure.",
    #地天泰
    f"{yin}\n{yin}\n{yin}\n{yang}\n{yang}\n{yang}": 
    "TEXT：Family relationships are harmonious, and everything seems to be going well. However, it is important to be mindful of gains and losses—acting recklessly could bring misfortune.",



    # 天泽履
    f"{yang}\n{yang}\n{yang}\n{yin}\n{yang}\n{yang}": 
    "TEXT：Be cautious in everything you do—challenges may arise, but with careful handling and humility, you can turn things around and achieve a good outcome.",
    #兑为泽 
    f"{yin}\n{yang}\n{yang}\n{yin}\n{yang}\n{yang}": 
     """TEXT：You are smart, outgoing, quick-witted, and kind-hearted, with a strong sense of public service and leadership skills, 
        making it easier for you to take on leadership roles. However, always stay fair and just, avoid flattery or abusing power, remain humble, 
        and be cautious of overconfidence to prevent being misled by the wrong people.""",
    #火泽睽
    f"{yang}\n{yin}\n{yang}\n{yin}\n{yang}\n{yang}": 
    "TEXT：You are full of contradictions and opposites, so it's important to stay calm, open-minded, and adaptable to move forward smoothly.",    
    #雷泽归妹
    f"{yin}\n{yin}\n{yang}\n{yin}\n{yang}\n{yang}": 
    "TEXT：A new phase is approaching, bringing big changes—it's crucial to have a broad vision and recognize the pros, cons, and potential outcomes.",  
    #风泽中孚
    f"{yang}\n{yang}\n{yin}\n{yin}\n{yang}\n{yang}": 
    "TEXT：Always treat people with honesty and handle matters with integrity, and everything will go well. However, if you harbor dishonest intentions, misfortune will follow.",  
    #水泽节
    f"{yin}\n{yang}\n{yin}\n{yin}\n{yang}\n{yang}": 
    "TEXT：Ambitions cannot be fully realized at the moment, so it is important to exercise restraint in all matters. Avoid excess in everything, especially alcohol and indulgence.",  
    #山泽损
    f"{yang}\n{yin}\n{yin}\n{yin}\n{yang}\n{yang}": 
    "TEXT：Things are not going smoothly right now, and there are signs of financial loss. However, although there may be losses at first, they could turn out to be a blessing in disguise, bringing benefits later.", 
    #地泽临
    f"{yin}\n{yin}\n{yin}\n{yin}\n{yang}\n{yang}": 
    "TEXT：Everything is going smoothly, and there is harmony between all aspects. The future looks promising, but it is best not to rush things too quickly.", 


    #天火同人
    f"{yang}\n{yang}\n{yang}\n{yang}\n{yin}\n{yang}": 
    "TEXT：You are cheerful and optimistic, friendly and outgoing, with strong social skills and good relationships with others. Works well in a team and competes fairly, you will get the rewards you deserve.",    
    #泽火革
    f"{yin}\n{yang}\n{yang}\n{yang}\n{yin}\n{yang}": 
    "TEXT：Everything is constantly changing, so it is best to let go of the old and embrace the new in order to adapt to change. This is a time for transformation and renewal.",    
    #离为火
    f"{yang}\n{yin}\n{yang}\n{yang}\n{yin}\n{yang}": 
    "TEXT：Everything looks great on the surface, like the scorching sun at its peak. However, this is not the time to rush or act impulsively.",    
    #雷火丰
    f"{yin}\n{yin}\n{yang}\n{yang}\n{yin}\n{yang}": 
    "TEXT：Your luck is extremely strong, and it is a time of great harvest. However, do not be too greedy—appreciate what you have. Be cautious of disputes, financial losses, and even fire hazards.",    
    #风火家人
    f"{yang}\n{yang}\n{yin}\n{yang}\n{yin}\n{yang}": 
    "TEXT：Everything will go smoothly and bring good fortune. Working with others will lead to success, and there may be joyful events like weddings or the arrival of a new family member.",    
    #水火既济
    f"{yin}\n{yang}\n{yin}\n{yang}\n{yin}\n{yang}": 
    "TEXT：It is a sign of success, bringing both fame and fortune. However, be cautious, as extreme prosperity may lead to downfall—things may start well but could end badly.",    
    #山火贲
    f"{yang}\n{yin}\n{yin}\n{yang}\n{yin}\n{yang}": 
    "TEXT：Looking good on the surface but lacking substance inside will not get you far. It is important to keep improving yourself and approach everything in a steady and methodical way.",    
    #地火明夷
    f"{yin}\n{yin}\n{yin}\n{yang}\n{yin}\n{yang}": 
    "TEXT：Obstacles are everywhere, and troublemakers may cause harm, making it easy to feel confused. It is best to stay patient, hold your ground, and wait for the right moment to take action.", 


    #天雷无妄
    f"{yang}\n{yang}\n{yang}\n{yin}\n{yin}\n{yang}": 
    "TEXT：One should always act with integrity. If someone behaves dishonorably, they will eventually face misfortune.",    
    #火雷噬嗑
    f"{yang}\n{yin}\n{yang}\n{yin}\n{yin}\n{yang}": 
    "TEXT：Obstacles and conflicts are inevitable. It is best to stick to the usual rules and not be tempted by profit, as the problem will eventually be resolved.",    
    #泽雷随
    f"{yang}\n{yin}\n{yin}\n{yin}\n{yin}\n{yang}": 
    "TEXT：This is a sign of getting rid of the old and welcoming the new. It is best to work with others for great rewards, but avoid being indecisive or acting alone.",    
    #震为雷
    f"{yin}\n{yin}\n{yang}\n{yin}\n{yin}\n{yang}": 
    "TEXT：On the surface, everything looks prosperous and impressive, but beneath it, things are turbulent and unstable, full of challenges.",    
    #风雷益
    f"{yang}\n{yang}\n{yin}\n{yin}\n{yin}\n{yang}": 
    "TEXT：Right now, luck is on your side, and with the help of influential people, you can achieve success. It is best to be generous and help others because giving is more rewarding than receiving.",    
    #水雷屯
    f"{yin}\n{yang}\n{yin}\n{yin}\n{yin}\n{yang}": 
    "TEXT：At first, things may not go smoothly, but you need to face challenges head-on, stay cautious yet determined, and adapt flexibly to the situation. Success is possible if you seize the right moment, but do not rush—there will still be obstacles, and support from others will be crucial, so always be generous and build goodwill in advance.",    
    #山雷颐
    f"{yang}\n{yin}\n{yin}\n{yin}\n{yin}\n{yang}": 
    "TEXT：Handle matters with careful consideration and avoid scheming against others. Stay on the right path and act with kindness to achieve good outcomes.",    
    #地雷复
    f"{yin}\n{yin}\n{yin}\n{yin}\n{yin}\n{yang}": 
    "TEXT：This is a sign of good fortune and smooth progress. Rushing things will not help, so take it step by step, and success will come.",    


    # 天风姤
    f"{yang}\n{yang}\n{yang}\n{yang}\n{yang}\n{yin}": 
    "TEXT：Be cautious of romantic entanglements, as things may not go smoothly. It is best to act carefully in all matters.",
    # 泽风大过
    f"{yin}\n{yang}\n{yang}\n{yang}\n{yang}\n{yin}": 
    "TEXT：Your career is facing hidden risks, possibly even serious crises, so you must be extremely cautious. Stay balanced, remain humble and approachable, think boldly but act carefully, and seek help from others when needed. If necessary, do not be afraid to take unconventional approaches and take calculated risks.",
    # 火风鼎
    f"{yang}\n{yin}\n{yang}\n{yang}\n{yang}\n{yin}": 
    "TEXT：Luck is still on your side, and your career has a good chance of success. However, do not delay important matters, and be cautious of potential legal disputes.",
    # 雷风恒
    f"{yin}\n{yin}\n{yang}\n{yang}\n{yang}\n{yin}": 
    "TEXT：Everything will go smoothly, and success will come with consistent effort. Stay grounded and follow the right path, but acting recklessly may bring trouble.",
    # 巽为风
    f"{yang}\n{yang}\n{yin}\n{yang}\n{yang}\n{yin}": 
    "TEXT：There will be many ups and downs, and your luck will be unpredictable. Stay adaptable, keep a calm mind, and hold firmly to what is right.",
    # 水风井
    f"{yin}\n{yang}\n{yin}\n{yang}\n{yang}\n{yin}": 
    "TEXT：If you cannot take the initiative and lack drive, it is better to stay calm and go with the flow. Sometimes, patience brings better results than forcing things.",
    # 山风蛊
    f"{yang}\n{yin}\n{yin}\n{yang}\n{yang}\n{yin}": 
    "TEXT：Things are not going well, and challenges are causing confusion. It is best to make bold changes; otherwise, both internal and external troubles may arise.",
    # 地风升
    f"{yin}\n{yin}\n{yin}\n{yang}\n{yang}\n{yin}": 
    "TEXT：Everything is going smoothly, continuously progressing, and steadily moving forward with great prospects. However, it is important to develop step by step and not rush ahead just because things are going well.",


    # 天水讼
    f"{yang}\n{yang}\n{yang}\n{yin}\n{yang}\n{yin}": 
    "TEXT：Things are not going as planned, and nothing seems to be going smoothly. Be cautious of people with bad intentions and watch out for traps.",
    # 泽水困
    f"{yin}\n{yang}\n{yang}\n{yin}\n{yang}\n{yin}": 
    "TEXT：The situation is extremely difficult, and life is facing a huge challenge. If you take dishonest shortcuts, you will only sink deeper. However, if you stay strong, hold onto your principles, and face adversity with resilience, you will eventually succeed.",
    # 火水未济
    f"{yang}\n{yin}\n{yang}\n{yin}\n{yang}\n{yin}": 
    "TEXT：The situation is extremely difficult, and life is facing a huge challenge. If you take dishonest shortcuts, you will only sink deeper. However, if you stay strong, hold onto your principles, and face adversity with resilience, you will eventually succeed.",
    # 雷水解
    f"{yin}\n{yin}\n{yang}\n{yin}\n{yang}\n{yin}": 
    "TEXT：Your energy is starting to recover, so it is best to take things easy, rest, and maintain a calm and steady approach. Once you are fully prepared, take action immediately and seize the opportunity, but do not be greedy—focus on what truly benefits you.",
    # 风水涣
    f"{yang}\n{yang}\n{yin}\n{yin}\n{yang}\n{yin}": 
    "TEXT：Although there may be challenges and difficulties, they can eventually be resolved, leading to success in all matters. However, avoid being careless or acting impulsively.",
    # 坎为水
    f"{yin}\n{yang}\n{yin}\n{yin}\n{yang}\n{yin}": 
    "TEXT：Challenges are everywhere, so stay calm and handle them wisely. Keep a positive mindset and avoid unnecessary conflicts with others.",
    # 山水蒙
    f"{yang}\n{yin}\n{yin}\n{yin}\n{yang}\n{yin}": 
    "TEXT：At first, you may feel lost and uncertain about which direction to take. Be patient, wait for the right moment to act, and listen to others' advice to find a clear path forward.",
    # 地水师
    f"{yin}\n{yin}\n{yin}\n{yin}\n{yang}\n{yin}": 
    "TEXT：There will be many challenges ahead, so always follow the proper way of doing things. Avoid making reckless decisions or taking shortcuts, and be cautious of hidden opponents.",


    # 天山遁
    f"{yang}\n{yang}\n{yang}\n{yang}\n{yin}\n{yin}": 
    "TEXT：When petty people thrive, noble people decline. In such times, it is better to step back rather than push forward. When facing difficulties, focus on self-improvement and personal growth.",
    # 泽山咸
    f"{yin}\n{yang}\n{yang}\n{yang}\n{yin}\n{yin}": 
    "TEXT：Everything is going smoothly, bringing good fortune. However, do not let yourself be overwhelmed by emotions from an improper relationship.",
    # 火山旅
    f"{yang}\n{yin}\n{yang}\n{yang}\n{yin}\n{yin}": 
    "TEXT：Everything is uncertain and constantly changing, so it is best to stay confident and seek advice from others. Otherwise, misfortune is likely to follow.",
    # 雷山小过
    f"{yin}\n{yin}\n{yang}\n{yang}\n{yin}\n{yin}": 
    "TEXT：Things are not going well, so it is better to focus on small tasks rather than big ones. Be especially careful, as even small mistakes could cause trouble or lead to disputes.",
    # 风山渐
    f"{yang}\n{yang}\n{yin}\n{yang}\n{yin}\n{yin}": 
    "TEXT：You are gradually moving towards a bright future. It is a good time to lay a solid foundation for success, but be cautious of potential troubles related to romance and mistakes in important documents.",
    # 水山蹇
    f"{yin}\n{yang}\n{yin}\n{yang}\n{yin}\n{yin}": 
    "TEXT：It is a time full of difficulties and challenges, where every step forward or backward seems troublesome. The best approach is to stay on the right path and avoid reckless actions, as any impulsive move may bring misfortune.",
    # 艮为山
    f"{yang}\n{yin}\n{yin}\n{yang}\n{yin}\n{yin}": 
    "TEXT：Do not act recklessly. The path ahead is blocked, so it is best to wait for the right opportunity to move forward.",
    # 地山谦
    f"{yin}\n{yin}\n{yin}\n{yang}\n{yin}\n{yin}": 
    "TEXT：Good fortune and safety are ahead, with limitless opportunities. However, one must stay humble and avoid arrogance.",


    # 天地否
    f"{yang}\n{yang}\n{yang}\n{yin}\n{yin}\n{yin}": 
    "TEXT：Things are not going smoothly, and nothing seems to be working out. It is best to stay patient and endure for now, as difficult times will eventually pass, leading to better days.",
    # 泽地萃
    f"{yin}\n{yang}\n{yang}\n{yin}\n{yin}\n{yin}": 
    "TEXT：Good fortune is on your side, and with the support of elders, your career will thrive. However, be cautious of financial disputes.",
    # 火地晋
    f"{yang}\n{yin}\n{yang}\n{yin}\n{yin}\n{yin}": 
    "TEXT：Career, reputation, and financial luck are all favorable. It is a sign of promotion and success.",
    # 雷地豫
    f"{yin}\n{yin}\n{yang}\n{yin}\n{yin}\n{yin}": 
    "TEXT：Everything will go smoothly, and you may receive support from elders. However, be cautious of troubles related to relationships and always be prepared for challenges.",
    # 风地观
    f"{yang}\n{yang}\n{yin}\n{yin}\n{yin}\n{yin}": 
    "TEXT：In times of change, it is important to stay observant and pay close attention to details. You may feel troubled, so be cautious and avoid external temptations.",
    # 水地比
    f"{yin}\n{yang}\n{yin}\n{yin}\n{yin}\n{yin}": 
    "TEXT：Everything will go smoothly, and you may receive support from influential people. Act quickly and decisively, as hesitation could cost you opportunities.",
    # 山地剥
    f"{yang}\n{yin}\n{yin}\n{yin}\n{yin}\n{yin}": 
    "TEXT：Misfortune is looming, so it is best to reconsider your plans. Avoid acting too clever, and be cautious of being dragged into trouble by women or deceitful people.",
   # 坤为地
    f"{yin}\n{yin}\n{yin}\n{yin}\n{yin}\n{yin}": 
    "Do not rush into things; it is better to stay calm and act cautiously. Sometimes, waiting and observing will lead to the best outcome.",
    
}

original_key = Original_6_lines.strip()
changed_key = Changed_6_lines.strip()

print("Original_6_lines：")
print(Original_6_lines)
if original_key in text_dict:
    print("Original result：")
    print(text_dict[original_key])
else:
    print("No correspond text")

#changed 6 lines
print("Changed_6_lines：")
print(Changed_6_lines)
if changed_key in text_dict:
    print("Changed result：")
    print(text_dict[changed_key])
else:
    print("No correspond text")