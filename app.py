from flask import Flask, request, render_template

app = Flask(__name__)

price = 1000
discount_used = False

@app.route("/", methods=["GET","POST"])
def shop():
    global price
    global discount_used

    message = ""

    if request.method == "POST":

        discount = int(request.form.get("discount"))

        # BUSINESS LOGIC FLAW
        # Server trusts user supplied discount
        price = price - discount

        if price < 0:
            message = "Congratulations! Item is free."
        else:
            message = "Discount Applied!"

    return render_template("shop.html", price=price, message=message)

if __name__ == "__main__":
    app.run(debug=True)