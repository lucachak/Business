from django.shortcuts import Http404, render

# Dados dos Projetos Reais
PROJECTS_DATA = {
    1: {
        "title": "CourierIQ",
        "subtitle": "Logistics & Delivery Tracking",
        "description": "Sistema inteligente de gestão de entregas e rastreamento. Focado na otimização de rotas e status em tempo real para transportadoras e clientes finais. Arquitetura modular pronta para escala.",
        "tags": ["Python", "Django", "Tracking API", "Logistics"],
        "image": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1000&auto=format&fit=crop",  # Foto de container/logística
        "github_url": "https://github.com/lucachak/CourierIQ",
    },
    2: {
        "title": "Online Courses",
        "subtitle": "LMS Education Platform",
        "description": "Plataforma de ensino a distância (LMS) completa. Gerenciamento de alunos, upload de aulas e acompanhamento de progresso. Desenvolvido com foco na experiência do usuário e entrega de conteúdo multimídia.",
        "tags": ["Django", "Education", "Streaming", "User Mgmt"],
        "image": "https://images.unsplash.com/photo-1501504905252-473c47e087f8?q=80&w=1000&auto=format&fit=crop",  # Foto de estudos/café
        "github_url": "https://github.com/lucachak/Online-courses",
    },
    3: {
        "title": "Store Core",
        "subtitle": "E-commerce Architecture",
        "description": "Backend robusto para comércio eletrônico. Inclui gestão de inventário, carrinho de compras e integração segura de pagamentos. Estrutura preparada para alta concorrência de transações.",
        "tags": ["E-commerce", "Payment Gateway", "Security", "SQL"],
        "image": "https://images.unsplash.com/photo-1556742049-0cfed4f7a07d?q=80&w=1000&auto=format&fit=crop",  # Foto de tecnologia/pagamento
        "github_url": "https://github.com/lucachak/Store",
    },
    4: {
        "title": "Hotel Manager",
        "subtitle": "Hotel Management Architecture",
        "description": "Backend robusto para gestao de hotel. Inclui gestão de inventário,comandas e integração segura de pagamentos",
        "tags": ["Hotel", "CRM", "Security", "PostgreSQL"],
        "image": "https://images.unsplash.com/photo-1556742049-0cfed4f7a07d?q=80&w=1000&auto=format&fit=crop",  # Foto de tecnologia/pagamento
        "github_url": "https://ik4kukb02n.onrender.com/",
    },
}


def index(request):
    return render(request, "index.html")


def project_detail(request, project_id):
    project = PROJECTS_DATA.get(project_id)
    if not project:
        raise Http404("Project not found")

    return render(request, "partials/project_modal.html", {"project": project})
