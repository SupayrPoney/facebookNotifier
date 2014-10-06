import fbconsole

fbconsole.ACCESS_TOKEN = "sdhgqsfguypiùmsbqdhv"

for notif in fbconsole.iter_pages(fbconsole.get("/me/notifications")):
    print notif
