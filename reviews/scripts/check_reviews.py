from reviews.models import Review


def check_reviews():
    stop_words = ["bad", "test"]
    reviews = Review.objects.filter(status='in_waiting')
    block_reason = ''
    for review in reviews:
        for w in review.subject.split():
            if w in stop_words:
                block_reason = "There are stop words in the subject\n"
                break
        for w in review.text.split():
            if w in stop_words:
                block_reason = "There are stop words in the text\n"
                break
        if block_reason:
            review.block_reason = block_reason
            review.save()
