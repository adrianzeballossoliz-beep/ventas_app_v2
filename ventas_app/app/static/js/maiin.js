// Sistema de Análisis de Ventas — main.js

// Auto-cerrar alertas después de 4 segundos
document.addEventListener('DOMContentLoaded', function () {

    // Auto-dismiss alerts
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            bsAlert.close();
        }, 4000);
    });

    // Activar tooltips de Bootstrap
    const tooltipEls = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltipEls.forEach(function (el) {
        new bootstrap.Tooltip(el);
    });

    // Resaltar fila de tabla al hacer hover
    const rows = document.querySelectorAll('tbody tr');
    rows.forEach(function (row) {
        row.addEventListener('mouseenter', function () {
            this.style.cursor = 'pointer';
        });
    });

    // Animación de entrada para las KPI cards
    const kpiCards = document.querySelectorAll('.kpi-card');
    kpiCards.forEach(function (card, index) {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        setTimeout(function () {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });

    // Mostrar la hora actual en el navbar si existe el elemento
    const clockEl = document.getElementById('reloj');
    if (clockEl) {
        function actualizarReloj() {
            const now = new Date();
            clockEl.textContent = now.toLocaleTimeString('es-BO', { hour: '2-digit', minute: '2-digit' });
        }
        actualizarReloj();
        setInterval(actualizarReloj, 60000);
    }

});