from django.shortcuts import render

# Create your views here.
def homeNotas(request):
    print(request.POST)
    mensagens = ''
    
    if request.method == "POST":
        lingua = request.POST['Nota1']
        Natureza = request.POST['Nota2']
        Humanas = request.POST['Nota3']
        tecnologias = request.POST['Nota4']
        Redação = request.POST['Nota5']
        
        mensagens = list()
        if lingua == '': lingua = 0
        if int(lingua) > 1000:
            mensagens.append( 'valor invalido')
            
        
        
    
    contex = {
        "messages":mensagens
    }
    return render(request, 'CalcularNotas/home.html',context=contex)