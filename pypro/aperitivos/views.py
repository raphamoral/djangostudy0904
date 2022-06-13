from django.shortcuts import render

class Video:
    def __init__(self,slug, titulo,youtube_id):
        self.titulo =titulo
        self.slug= slug
        self.youtube_id= youtube_id

# Create your views here.
videos = [Video( 'motivacao',  "Video Aperitivo: Motivação","_UfhOwkwXZ4"),
          Video( "poo-ramalho", "Programação Orientada a Objetos - Com Luciano Ramalho",
            "_EblOW9nfkNA")]
videos_dct = {v.slug: v for v in videos}

def indice(request):
    return render(request, "aperitivos/indice.html", context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, "aperitivos/video.html", context={"video": video})
