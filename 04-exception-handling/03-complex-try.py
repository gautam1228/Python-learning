def serve_icecream(flavour: str):
    try:
        print(f"Serving {flavour} ice cream ...")
        if flavour.lower() == "unknown":
            raise ValueError("We don't know that flavour.")

    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavour} ice cream is served :)")
    finally:
        print("\n--- Next customer please ---\n")


serve_icecream("Chocolate")
serve_icecream("uNknown")
