data = {"media": input("Enter type: ")}

match data["media"]:
    case "video":
        print("It's video")
    case "photo":
        print("It's photo")