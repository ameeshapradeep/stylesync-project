from flask import Flask, render_template, request

app = Flask(__name__)

def generate_palette(base_color):
    return {
        "primary": base_color,
        "light": base_color + "33",
        "dark": base_color + "cc",
    }

def get_doodle(theme, custom_url):
    if custom_url:
        return custom_url

    theme = theme.lower()

    if theme == "love":
        return "https://cdn-icons-png.flaticon.com/512/833/833472.png"
    elif theme == "space":
        return "https://cdn-icons-png.flaticon.com/512/3212/3212608.png"
    elif theme == "tech":
        return "https://cdn-icons-png.flaticon.com/512/1055/1055687.png"
    elif theme == "nature":
        return "https://cdn-icons-png.flaticon.com/512/415/415733.png"
    else:
        return ""

@app.route("/", methods=["GET", "POST"])
def index():
    color = "#667eea"
    title = "Card Title"
    content = "This is a preview card"
    theme = ""
    doodle = ""
    font = "Arial"
    custom_url = ""

    if request.method == "POST":
        color = request.form.get("color")
        title = request.form.get("title")
        content = request.form.get("content")
        theme = request.form.get("theme")
        font = request.form.get("font")
        custom_url = request.form.get("custom_url")

        doodle = get_doodle(theme, custom_url)

    palette = generate_palette(color)

    return render_template(
        "index.html",
        palette=palette,
        title=title,
        content=content,
        doodle=doodle,
        font=font
    )

if __name__ == "__main__":
    app.run(debug=True)