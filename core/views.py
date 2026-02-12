from django.shortcuts import Http404, render

# Simulação de Banco de Dados
PROJECTS_DATA = {
    1: {
        "title": "Fintech Core",
        "subtitle": "High-frequency trading platform",
        "description": "Uma arquitetura de baixa latência projetada para processar milhões de transações por segundo. Utilizamos C++ para o núcleo de execução e Python para a camada de análise de dados, garantindo precisão de microssegundos.",
        "tags": ["C++", "Python", "AWS", "Low Latency"],
        "image": "https://images.unsplash.com/photo-1611974765270-ca1258634369?q=80&w=1000&auto=format&fit=crop", # Imagem placeholder abstrata
    },
    2: {
        "title": "Health Data",
        "subtitle": "AI-driven diagnostics",
        "description": "Sistema de criptografia ponta a ponta para dados sensíveis de pacientes, integrado a uma rede neural que auxilia no diagnóstico precoce de patologias através de análise de imagem.",
        "tags": ["AI/ML", "Cryptography", "HIPAA Compliant"],
        "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?q=80&w=1000&auto=format&fit=crop",
    },
    3: {
        "title": "Urban Flow",
        "subtitle": "Smart city traffic management",
        "description": "Rede de sensores IoT conectada a um sistema central de processamento que otimiza o fluxo de semáforos em tempo real, reduzindo o congestionamento urbano em até 30%.",
        "tags": ["IoT", "Real-time Data", "GoLang"],
        "image": "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=1000&auto=format&fit=crop",
    }
}

def index(request):
    return render(request, "index.html")

def project_detail(request, project_id):
    project = PROJECTS_DATA.get(project_id)
    if not project:
        raise Http404("Project not found")
    
    # Retorna apenas o pedaço de HTML (Partial)
    return render(request, "partials/project_modal.html", {"project": project})
