document.addEventListener('DOMContentLoaded', () => {
    // --- 1. LÓGICA DO MENU ---
    const hamburger = document.getElementById('hamburger-btn');
    const menuOverlay = document.getElementById('menu-overlay');
    const menuLinks = document.querySelectorAll('.menu-links a');

    // Função para abrir/fechar menu
    const toggleMenu = () => {
        if(hamburger && menuOverlay) {
            hamburger.classList.toggle('active');
            menuOverlay.classList.toggle('active');
        }
    };

    if (hamburger) {
        hamburger.addEventListener('click', toggleMenu);
    }

    // Fecha o menu ao clicar em qualquer link
    menuLinks.forEach(link => {
        link.addEventListener('click', () => {
            // Fecha o menu
            toggleMenu();
            // O efeito de scroll acontece via CSS (scroll-behavior: smooth)
        });
    });
});

// --- 2. LÓGICA DO THREE.JS (GLOBO) ---
let scene, camera, renderer, landMesh, oceanMesh;
const container = document.getElementById("globe-3d");

function init3D() {
    if (!container) return;

    scene = new THREE.Scene();
    
    camera = new THREE.PerspectiveCamera(
        40,
        container.clientWidth / container.clientHeight,
        0.1,
        1000
    );
    camera.position.z = 6.5;

    renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setClearColor(0x000000, 0);
    container.appendChild(renderer.domElement);

    const ambientLight = new THREE.AmbientLight(0xffffff, 1.0);
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 1.0);
    directionalLight.position.set(5, 5, 5);
    scene.add(directionalLight);

    // Oceano
    const oceanGeo = new THREE.SphereGeometry(1.98, 64, 64);
    const oceanMat = new THREE.MeshStandardMaterial({
        color: 0xe2e8f0,
        roughness: 0.6,
        metalness: 0.1,
    });
    oceanMesh = new THREE.Mesh(oceanGeo, oceanMat);
    scene.add(oceanMesh);

    // Países
    const landGeo = new THREE.SphereGeometry(2, 64, 64);
    const textureLoader = new THREE.TextureLoader();
    const alphaMap = textureLoader.load(
        "https://raw.githubusercontent.com/mrdoob/three.js/master/examples/textures/planets/earth_specular_2048.jpg"
    );

    const landMat = new THREE.MeshStandardMaterial({
        color: 0x222222,
        alphaMap: alphaMap,
        transparent: true,
        side: THREE.DoubleSide,
        roughness: 0.9,
        metalness: 0.0,
    });

    landMesh = new THREE.Mesh(landGeo, landMat);
    scene.add(landMesh);

    onWindowResize();
    animate();
}

function animate() {
    requestAnimationFrame(animate);
    if (landMesh) landMesh.rotation.y += 0.001;
    if (oceanMesh) oceanMesh.rotation.y += 0.001;
    renderer.render(scene, camera);
}

function onWindowResize() {
    if (!container || !camera || !renderer) return;
    const width = container.clientWidth;
    const height = container.clientHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
}

window.addEventListener("resize", onWindowResize, false);
window.addEventListener("load", init3D);
