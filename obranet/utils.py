import reflex as rx

# Común

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


# preview = "https://moure.dev/preview.jpg"

# _meta = [
#     {"name": "og:type", "content": "website"},
#     {"name": "og:image", "content": preview},
#     {"name": "twitter:card", "content": "summary_large_image"},
#     {"name": "twitter:site", "content": "@mouredev"}
# ]

# Index

index_title = "Obranet"
# index_description = "Hola, mi nombre es Brais Moure. Soy ingeniero de software, desarrollador freelance full-stack y divulgador."

# index_meta = [
#     {"name": "og:title", "content": index_title},
#     {"name": "og:description", "content": index_description},
# ]
# index_meta.extend(_meta)



# Registre

register_title = "Obranet | Registro"
# register_description = "Hola, mi nombre es Brais Moure. Soy ingeniero de software, desarrollador freelance full-stack y divulgador."

# register_meta = [
#     {"name": "og:title", "content": register_title},
#     {"name": "og:description", "content": register_description},
# ]
# register_meta.extend(_meta)