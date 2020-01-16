def getPopularProducts():
    return [
        { "_id": "23978", "brand": "8x4", "category": "Gezond & verzorging", "deeplink": "https://www.opisopvoordeelshop.nl/8x4-men-men-beast-deospray-150ml" },
        { "_id": "7225", "brand": "8x4", "category": "Gezond & verzorging", "deeplink": "https://www.opisopvoordeelshop.nl/8x4-heavenly-deospray-150ml" },
        { "_id": "29438", "brand": "1Auto", "category": "Wonen & vrije tijd", "deeplink": "https://www.opisopvoordeelshop.nl/1auto-ruitensproeiervloeistof-zomer-4000ml" },
        { "_id": "9196", "brand": "8x4", "category": "Gezond & verzorging", "deeplink": "https://www.opisopvoordeelshop.nl/8x4-for-men-urban-spirit-150-ml"},
        { "_id": "8570", "brand": "8x4", "category": "Gezond & verzorging", "deeplink": "https://www.opisopvoordeelshop.nl/8x4-unity-150-ml"},
        { "_id": "22309", "brand": "Agfa", "category": "Elektronica & media", "deeplink": "https://www.opisopvoordeelshop.nl/afgaphoto-alkaline-power-batterijen-aa-4-stuks"}
    ]

def getPersonalProducts(session):
    print("Recommendations for session: {}".format(session['_id']))

    return [
        {"_id": "23978", "brand": "8x4", "category": "Gezond & verzorging", "deeplink": "https://www.opisopvoordeelshop.nl/8x4-men-men-beast-deospray-150ml"},
        {"_id": "22309", "brand": "Agfa", "category": "Elektronica & media", "deeplink": "https://www.opisopvoordeelshop.nl/afgaphoto-alkaline-power-batterijen-aa-4-stuks"}
    ]