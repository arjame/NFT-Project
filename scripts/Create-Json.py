# This script is simply creates json files from the dictionary which is put here
import json

metadata_template = {
    "Agircola": {
        "name": "Agircola",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmaoT2hFK21gPHZ75hdJsRXyjTmaupWaWend5YqbZMKjko?filename=Agircola.png",
    },
    "Aimo": {
        "name": "Aimo",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmQaDGgvhQowt6TNZLUVGpNTGK2SDMmsxgwUziBW8zWi62?filename=Aimo.png",
    },
    "Bargigli_Alpi": {
        "name": "Bargigli_Alpi",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmectL7urynadJg17GYL8LcQ9fo8QJ5UeT9REp8MBqr9Sp?filename=Bargigli_Alpi.png",
    },
    "Bargigli_Neos": {
        "name": "Bargigli_Neos",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmRjf7kPYEYeFhMok7yLQdqUfFdNP2CD6XCfMXbgq6DDZZ?filename=Bargigli_Neos.png",
    },
    "Beltramo": {
        "name": "Beltramo",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmbbK55cCVFAgAgEmVdgSPWxJo5J1Me6VqxnWFG83agWek?filename=Beltramo.png",
    },
    "Cafarella": {
        "name": "Cafarella",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmQX2LHP6i72fbCTu7NPfsUXDaZMWUA233x54WqrPizejx?filename=Cafarella.png",
    },
    "Cariani": {
        "name": "Cariani",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/Qmb3zNiDTmWejLxysh5ugFdEiHmKNLs1MXHsgr6XvxLjyH?filename=Cariani.png",
    },
    "Caruso": {
        "name": "Caruso",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmTTQtKHWSAZM5jA6ZF6LRkbN6mfpvKyp3DeEWH3vPNKQw?filename=Caruso.png",
    },
    "Ciuccarelli": {
        "name": "Ciuccarelli",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/Qmbz7DEpHhY2F4Uy4ra4DMgmNixeM9t3tirAavR1pRYkGK?filename=Ciuccarelli.png",
    },
    "Elicona": {
        "name": "Elicona",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmWNmWWcp15DqjGHXg491BRa5jaKNAi9BszC6n3E2PzcSk?filename=Elicona.png",
    },
    "Ferrero": {
        "name": "Ferrero",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmcDJKqYyWH3s9rxedKfLcbgAKKHKwYbPdLB4jKK26STm3?filename=Ferrero.png",
    },
    "Ferri": {
        "name": "Ferri",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmQvw2ssZLXsZMoQmpBjXMpQjBh29HEEttnue9JSMxRd97?filename=Ferri.png",
    },
    "Forti": {
        "name": "Forti",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmZfGU5VYTyKemJfw5v6YkbgRqnfFmefAowxubdzTt9BE2?filename=Forti.png",
    },
    "Gasparrini": {
        "name": "Gasparrini",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmSDs8FCZCH2jvLn23HQMeJVdLmX5oT5b8dA9cHBfC8oB4?filename=Gasparrini.png",
    },
    "Irrera": {
        "name": "Irrera",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/Qma1riTcz7iz6nZ3Qmg9rnnL354nKTbTs6g6z6evuBmYqz?filename=Irrera.png",
    },
    "Jame": {
        "name": "Jame",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmNwWuCraPTF7Cb3E3brJg2fDr9yu6S19ankMHAynVWcXz?filename=Jame.png",
    },
    "Olgiati": {
        "name": "Olgiati",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmahsxWou6iecZPbdTDJ9U6tHNUTDxUoyZQ1cDBnWqD2ra?filename=Olgiati.png",
    },
    "Palazzolo": {
        "name": "Palazzolo",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmfFTfmpQ9AQXQJoqfhgPtc99fzjGZV2HndWJ4TEM4UWZN?filename=Palazzolo.png",
    },
    "Quaranta": {
        "name": "Quaranta",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmUGxHcjLSBuGueL3jw5R99yt6fJ4cp1jmkSZzXwCFv9jy?filename=Quaranta.png",
    },
    "Sarnataro_Alpi": {
        "name": "Sarnataro_Alpi",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmZ3vELQfcEY12sp5sSuwrFc7p3wYPhoTKGvS2nLf5JsXa?filename=Sarnataro_Alpi.png",
    },
    "Sarnataro_Neos": {
        "name": "Sarnataro_Neos",
        "description": "Alpipunks",
        "image": "https://ipfs.io/ipfs/QmQ1Mz8r4WCFdjyWWX7KV8rBr6srVf16uu7fvFjGn8h9cw?filename=Sarnataro_Neos.png",
    },
}
uri = {
    "Agircola": "https://ipfs.io/ipfs/QmaoT2hFK21gPHZ75hdJsRXyjTmaupWaWend5YqbZMKjko?filename=Agircola.png",
    "Aimo": "https://ipfs.io/ipfs/QmQaDGgvhQowt6TNZLUVGpNTGK2SDMmsxgwUziBW8zWi62?filename=Aimo.png",
    "Bargigli_Alpi": "https://ipfs.io/ipfs/QmectL7urynadJg17GYL8LcQ9fo8QJ5UeT9REp8MBqr9Sp?filename=Bargigli_Alpi.png",
    "Bargigli_Neos": "https://ipfs.io/ipfs/QmRjf7kPYEYeFhMok7yLQdqUfFdNP2CD6XCfMXbgq6DDZZ?filename=Bargigli_Neos.png",
    "Beltramo": "https://ipfs.io/ipfs/QmbbK55cCVFAgAgEmVdgSPWxJo5J1Me6VqxnWFG83agWek?filename=Beltramo.png",
    "Cafarella": "https://ipfs.io/ipfs/QmQX2LHP6i72fbCTu7NPfsUXDaZMWUA233x54WqrPizejx?filename=Cafarella.png",
    "Cariani": "https://ipfs.io/ipfs/Qmb3zNiDTmWejLxysh5ugFdEiHmKNLs1MXHsgr6XvxLjyH?filename=Cariani.png",
    "Caruso": "https://ipfs.io/ipfs/QmTTQtKHWSAZM5jA6ZF6LRkbN6mfpvKyp3DeEWH3vPNKQw?filename=Caruso.png",
    "Ciuccarelli": "https://ipfs.io/ipfs/Qmbz7DEpHhY2F4Uy4ra4DMgmNixeM9t3tirAavR1pRYkGK?filename=Ciuccarelli.png",
    "Elicona": "https://ipfs.io/ipfs/QmWNmWWcp15DqjGHXg491BRa5jaKNAi9BszC6n3E2PzcSk?filename=Elicona.png",
    "Ferrero": "https://ipfs.io/ipfs/QmcDJKqYyWH3s9rxedKfLcbgAKKHKwYbPdLB4jKK26STm3?filename=Ferrero.png",
    "Ferri": "https://ipfs.io/ipfs/QmQvw2ssZLXsZMoQmpBjXMpQjBh29HEEttnue9JSMxRd97?filename=Ferri.png",
    "Forti": "https://ipfs.io/ipfs/QmZfGU5VYTyKemJfw5v6YkbgRqnfFmefAowxubdzTt9BE2?filename=Forti.png",
    "Gasparrini": "https://ipfs.io/ipfs/QmSDs8FCZCH2jvLn23HQMeJVdLmX5oT5b8dA9cHBfC8oB4?filename=Gasparrini.png",
    "Irrera": "https://ipfs.io/ipfs/Qma1riTcz7iz6nZ3Qmg9rnnL354nKTbTs6g6z6evuBmYqz?filename=Irrera.png",
    "Jame": "https://ipfs.io/ipfs/QmNwWuCraPTF7Cb3E3brJg2fDr9yu6S19ankMHAynVWcXz?filename=Jame.png",
    "Olgiati": "https://ipfs.io/ipfs/QmahsxWou6iecZPbdTDJ9U6tHNUTDxUoyZQ1cDBnWqD2ra?filename=Olgiati.png",
    "Palazzolo": "https://ipfs.io/ipfs/QmfFTfmpQ9AQXQJoqfhgPtc99fzjGZV2HndWJ4TEM4UWZN?filename=Palazzolo.png",
    "Quaranta": "https://ipfs.io/ipfs/QmUGxHcjLSBuGueL3jw5R99yt6fJ4cp1jmkSZzXwCFv9jy?filename=Quaranta.png",
    "Sarnataro_Alpi": "https://ipfs.io/ipfs/QmZ3vELQfcEY12sp5sSuwrFc7p3wYPhoTKGvS2nLf5JsXa?filename=Sarnataro_Alpi.png",
    "Sarnataro_Neos": "https://ipfs.io/ipfs/QmQ1Mz8r4WCFdjyWWX7KV8rBr6srVf16uu7fvFjGn8h9cw?filename=Sarnataro_Neos.png",
}

for i in metadata_template:
    with open("./json/" + i + ".json", "w") as file:
        json.dump(metadata_template[i], file)
        print(file)
