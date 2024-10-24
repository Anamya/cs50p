from fpdf import FPDF

class Shirt():
    def __init__(self, name):
        self._pdf = FPDF(orientation="portrait", format="A4")
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 35)
        self._pdf.cell(0, 20,"CS50 Shirtificate",
                        new_x="LMARGIN", new_y="NEXT",align="C")
        self._pdf.image("shirtificate.png",w=self._pdf.epw)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(x=50, y=100, text=f"{name} took CS50")

    def save_pdf(self, name):
        self._pdf.output(name)


def main():
    name = input("Name: ")
    pdf = Shirt(name)
    pdf.save_pdf("shirtificate.pdf")

if __name__ == "__main__":
    main()
