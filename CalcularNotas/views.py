from django.shortcuts import render

# Create your views here.
def homeNotas(request):
    print(request.POST)
    mensagens = ''
    contex = {}
    
    if request.method == "POST":
        lingua = request.POST['Nota1']
        Natureza = request.POST['Nota2']
        Humanas = request.POST['Nota3']
        tecnologias = request.POST['Nota4']
        Redação = request.POST['Nota5']
        
        mensagens = list()
        if lingua == '' and lingua: lingua = 0
        if Natureza == '' and Natureza: Natureza = 0
        if Humanas == '' and Humanas: Humanas = 0
        if tecnologias == '' and tecnologias: tecnologias = 0
        if Redação == '' and Redação: Redação = 0
        
        is_invalido = (
            (int(lingua) < 1000) and (int(Natureza) < 1000) and (int(Humanas) < 1000) and (int(tecnologias) < 1000) and (int(Redação) < 1000) 
             )
        if not is_invalido:
            mensagens.append( 'valor invalido')
            contex = {
                 "messages":mensagens
                 }
        else:
            valor = (int(lingua) + int(Natureza) + int(Humanas) + int(tecnologias) + int(Redação) ) /5
            contex = {
                "messages":mensagens,
                "valor":int(valor)
            }
            
        
        
    
    
    return render(request, 'CalcularNotas/home.html',context=contex)