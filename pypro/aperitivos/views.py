from django.shortcuts import render

# Create your views here.
def video(request,slug):
    videos ={'motivacao':{"titulo": "Video Aperitivo: Motivação", "youtube_id":"_UfhOwkwXZ4"},
    'poo-ramalho':{"titulo": "Programação Orientada a Objetos - Com Luciano Ramalho", "youtube_id": "_EblOW9nfkNA"},}

    video =videos[slug]

    return render(request,"aperitivos/video.html", context={"video": video})