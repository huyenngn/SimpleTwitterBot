import threading
# from instagram_updates import InstagramUpdatesBot
from bots.translate_tweets import TranslateTweetsBot

bot_settings = {
    # twitter user the bot will automatically interact with
    "biases": ["srchafreen", "AngelssBecky"],
    # test users and admins
    "admins": ["FreenBeckyBot", "joohwangblink"],
    # twitter users and their respective emoji/alias
    # this could be accounts your biases regularily interact with
    # (including your biases)
    "twitter_handles": {
        "srchafreen": "\ud83d\udc30",
        "AngelssBecky": "\ud83e\udda6",
        "namorntaraaa": "\ud83d\udea2",
        "GAPtheseries": "\ud83d\udc69\ud83c\udffb\u200d\u2764\ufe0f\u200d\ud83d\udc8b\u200d\ud83d\udc69\ud83c\udffb",
    },
}

translation_settings = {
    # language settings
    "src": "th",
    "dst": "en",
    # replacements applied before translating
    "glossary": {
        "อะะ": " ahh",
        "ง้อ": "reconcile",
        "งอน": "sulking",
        "มุมุ": "kiss kiss",
        "มามี้": "Mami",
        "ยัก": "รัก",  # yak
        "ปีโย๊": "Piyo",
        "ฟรีนกี้": "Freenky",
        "ฟรีน": "Freen",
        "คุณสาม": "คุณแซม",  # Khun Sam
        "นุคน": "หนู",  # Nu -> Sandra
        "นุ": "หนู",
        "หนู": "แซนดร้า",
        "น้องพุง": "Nong Belly",
        "น้อง": "Nong",
        "พี่": "Phi",
        "ยัง": "",  # still/yet
        "อะ": "",  # a
    },
    # replacements applied after translating
    "corrections": {
        "Sandra": "Nu",
        "Beck ": "Bec ",
        "I am": "",
        "I'm ": "",
        "I ": "",
        " me ": " me/you ",
        " me.": " me/you.",
        "boyfriend": "girlfriend",
        " him ": " her ",
        " him.": " her.",
        "his ": "her ",
        "Mr.": "Khun",
    },
}


def main():
    ttb = TranslateTweetsBot(
        biases=bot_settings["biases"],
        src=translation_settings["src"],
        dst=translation_settings["dst"],
        glossary=translation_settings["glossary"],
        corrections=translation_settings["corrections"],
        admins=bot_settings["admins"],
        handles=bot_settings["twitter_handles"]
        )
    # ttb.tl.translate_image("https://pbs.twimg.com/media/FO3yZeYVsAEfBJx?format=jpg&name=large")
    # rules = ttb.create_rules()
    # ttb.delete_all_rules()
    # ttb.set_rules(rules)
    t_ttb = threading.Thread(target=ttb.start)
    t_ttb.start()
    # api = ttb.get_api()
    # iub = InstagramUpdatesBot(api=api)
    # t_iub = threading.Thread(target=iub.start)
    # t_iub.start()


if __name__ == "__main__":
    main()
