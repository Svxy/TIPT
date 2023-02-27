import tkinter as tk
from tkinter import messagebox
import requests


def track_ip():
    ip = ip_entry.get()
    if not ip:
        messagebox.showerror("Error", "Please enter an IP address")
        return
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        data = response.json()
        result_label.config(text=f"IP Address: {data['ip']}\n"
                                  f"Postal Code: {data['postal']}\n"
                                  f"City: {data['city']}\n"
                                  f"Region: {data['region']}\n"
                                  f"Country: {data['country']}\n"
                                  f"Organization: {data['org']}\n"
                                  f"Timezone: {data['timezone']}")
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Unable to get IP information")


def ping_ip():
    ip_address = ip_entry.get()
    url = f"https://www.isitdownrightnow.com/{ip_address}.html"

    try:
        response = requests.get(url)
        if "It's not just you!" in response.text:
            result_label.config(text="IP address is offline", fg="red")
        else:
            result_label.config(text="IP address is online", fg="green")
    except requests.exceptions.RequestException as e:
        result_label.config(text="Error checking online status", fg="red")


def check_vpn():
    ip = ip_entry.get()
    if not ip:
        messagebox.showerror("Error", "Please enter an IP address")
        return
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", headers={"User-Agent": "curl"})
        if "vpn" in response.text.lower() or "proxy" in response.text.lower():
            result_label.config(text=f"{ip} is using a VPN or proxy")
        else:
            result_label.config(text=f"{ip} is not using a VPN or proxy")
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Unable to check VPN")


def show_about():
    about_window = tk.Toplevel(window)
    about_window.title("About")
    about_window.iconbitmap("./assets/icon.ico")
    about_window.geometry("215x150")
    about_window.configure(bg="#2B2B2B")
    about_window.resizable(False, False)

    app_version_label = tk.Label(about_window, text="Version 1.1\nBe sure not to delete the assets folder.\nWould appreciate a taskbar pin!", bg="#2B2B2B", fg="white")
    app_version_label.pack(pady=10)

    app_creator_label = tk.Label(about_window, text="Created by TnyavnTo", bg="#2B2B2B", fg="white")
    app_creator_label.pack(pady=5)

    github_button = tk.Button(about_window, text="Visit GitHub", bg="#FF3333", fg="white",
                              command=lambda: open_url("https://github.com/svxy/tipt"))
    github_button.pack(pady=10)


def open_url(url):
    import webbrowser
    webbrowser.open(url)


window = tk.Tk()
window.title("TnyavnTos IP Tracker")
window.iconbitmap("./assets/icon.ico")
window.geometry("420x550")
window.configure(bg="#2B2B2B")
window.resizable(False, False)


app_title_label = tk.Label(window, text="TIPT\nTnyavnTos IP Tracker", font=("Impact", 18), bg="#2B2B2B", fg="white")
app_title_label.pack(pady=10)

logo = tk.PhotoImage(file="./assets/logo.png")
logo_label = tk.Label(window, image=logo, bg="#2B2B2B")
logo_label.pack()

ip_entry = tk.Entry(window, width=30, font=("Helvetica", 12))
ip_entry.pack(pady=10)

track_button = tk.Button(window, text="Track IP", font=("Helvetica", 12), bg="#FF3333", fg="white", command=track_ip)
track_button.pack(pady=10)

ping_button = tk.Button(window, text="Ping IP", font=("Helvetica", 12), bg="#FF3333", fg="white", command=ping_ip)
ping_button.pack(pady=5)

vpn_button = tk.Button(window, text="Check VPN", font=("Helvetica", 12), bg="#FF3333", fg="white", command=check_vpn)
vpn_button.pack(pady=5)

result_label = tk.Label(window, font=("Helvetica", 12), bg="#2B2B2B", fg="white")
result_label.pack(pady=10)

about_button = tk.Button(window, text="About", font=("Helvetica", 12), bg="#FF3333", fg="white", command=show_about)
about_button.pack(pady=80)

window.mainloop()