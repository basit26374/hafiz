def ayah_serializer(ayah):
    return {
        "ayah_number": ayah.ayah_number,
        "ayah_arabic": ayah.ayah_arabic[str(ayah.ayah_number)],
    }