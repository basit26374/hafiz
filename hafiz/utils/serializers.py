from hafiz.models.quran_sentence_text import QuranSentenceText as sent_text


def ayah_serializer(ayah):
    return {
        "ayad_id": ayah.id,
        "ayah_number": ayah.ayah_number,
        "ayah_arabic": ayah.ayah_arabic[str(ayah.ayah_number)],
    }


def variation_serializer(variation):
    sentence_object_list = [sent_text.query.filter(sent_text.id==sentence_id).with_entities(sent_text.sentence_arabic).all()[0][0]
        for sentence_id in variation.sentence_ids.split("-")]
    
    sentences = ""
    for sentence_object in sentence_object_list:
        for _, value in sentence_object.items():
            if sentences == "":
                sentences = f"{value}"
            else:
                sentences = f"{sentences} {value}"

    return{
        "id": variation.id,
        "variation_number": variation.variation_number,
        "sentences": sentences
    }


def words_serializer(word):
    return {
        "id": word[0],
        "arabic_word": word[1]
    }