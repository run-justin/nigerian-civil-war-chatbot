import difflib

knowledge = {
    "causes": """The Nigerian Civil War was caused by a combination of ethnic tensions, political instability, and military coups in 1966. 
The killing of political leaders and civilians, especially in the Northern region, created fear and mistrust. 
This led the Eastern Region, under Odumegwu Ojukwu, to declare independence as Biafra in 1967.""",

    "leaders": """The key leaders were Odumegwu Ojukwu, who led Biafra, and Yakubu Gowon, who was Nigeria’s Head of State. 
Other important figures included Nigerian military commanders and political leaders involved in the conflict.""",

    "start": """The Nigerian Civil War officially began on July 6, 1967, when Nigerian federal troops advanced into Biafra.""",

    "end": """The war ended in January 1970 when Biafran forces surrendered to the Nigerian government, leading to the reintegration of the Eastern Region.""",

    "effects": """The war caused massive humanitarian crises, including famine due to blockades. 
Millions of people died, and many were displaced. The war also had long-term political and economic effects on Nigeria.""",

    "famine": """One of the most devastating aspects of the war was famine in Biafra. 
The Nigerian blockade prevented food and medical supplies from entering, leading to widespread starvation, especially among children.""",

    "foreign": """Several foreign countries were involved indirectly. 
Britain and the Soviet Union supported Nigeria, while France showed sympathy toward Biafra. 
International organizations attempted to provide humanitarian aid.""",

    "events": """Major events included the declaration of Biafra in 1967, intense military battles, territorial changes, and humanitarian crises caused by blockades.""",

    "aftermath": """After the war, Nigeria adopted a policy of 'No Victor, No Vanquished' to promote unity. 
However, rebuilding and reconciliation took many years."""
}

keywords = {
    "causes": ["cause", "why", "reason", "origin", "led to"],
    "leaders": ["leader", "who", "command", "head"],
    "start": ["start", "begin", "when", "date"],
    "end": ["end", "finish", "stop"],
    "effects": ["effect", "impact", "result", "consequence"],
    "famine": ["famine", "starvation", "hunger", "food"],
    "foreign": ["foreign", "international", "countries", "support"],
    "events": ["event", "happen", "battle"],
    "aftermath": ["after", "result after", "post war"]
}


def find_best_match(user_input):
    user_input = user_input.lower()

    best_score = 0
    best_topic = None

    for topic, words in keywords.items():
        for word in words:
            score = difflib.SequenceMatcher(None, user_input, word).ratio()

            if word in user_input:
                score += 2

            if score > best_score:
                best_score = score
                best_topic = topic

    return best_topic


def ask_bot(user_input):
    topic = find_best_match(user_input)

    if topic:
        return knowledge[topic]
    else:
        return """I understand your question, but I need more context. 
Try asking about causes, leaders, famine, foreign involvement, or effects of the war."""
