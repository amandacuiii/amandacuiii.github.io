(function() {
    if (window.matchMedia('(hover: none)').matches) return;

    const style = document.createElement('style');
    style.textContent = `
        .cursor-dots {
            position: fixed;
            left: 0;
            top: 0;
            pointer-events: none;
            z-index: 9999;
        }
        .cursor-dots .dot {
            position: absolute;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #664930;
            transform: translate(-50%, -50%);
        }
    `;
    document.head.appendChild(style);

    const cursorDots = document.createElement('div');
    cursorDots.className = 'cursor-dots';
    cursorDots.id = 'cursor-dots';
    cursorDots.setAttribute('aria-hidden', 'true');
    document.body.insertBefore(cursorDots, document.body.firstChild);

    const dotCount = 12;
    const spacing = 8;
    const opacities = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.35, 0.28, 0.2, 0.12, 0.06];
    let targetX = -100, targetY = -100;
    let targetDirX = -1, targetDirY = 0;
    let mouseX = null, mouseY = null;
    const dirSmooth = 0.08;
    const posSmooth = 0.22;

    for (let i = 0; i < dotCount; i++) {
        const dot = document.createElement('span');
        dot.className = 'dot';
        dot.style.opacity = opacities[i];
        cursorDots.appendChild(dot);
    }
    const dots = cursorDots.querySelectorAll('.dot');
    const dotX = new Array(dotCount).fill(-100);
    const dotY = new Array(dotCount).fill(-100);
    let currX = -100, currY = -100;
    let currDirX = -1, currDirY = 0;

    document.addEventListener('mousemove', (e) => {
        const dx = mouseX !== null ? e.clientX - mouseX : 0;
        const dy = mouseY !== null ? e.clientY - mouseY : 0;
        mouseX = e.clientX;
        mouseY = e.clientY;
        targetX = e.clientX;
        targetY = e.clientY;
        const len = Math.sqrt(dx * dx + dy * dy);
        if (len > 1) {
            targetDirX = dx / len;
            targetDirY = dy / len;
        }
    });

    function animate() {
        currX += (targetX - currX) * posSmooth;
        currY += (targetY - currY) * posSmooth;
        currDirX += (targetDirX - currDirX) * dirSmooth;
        currDirY += (targetDirY - currDirY) * dirSmooth;
        const d = Math.sqrt(currDirX * currDirX + currDirY * currDirY) || 1;
        currDirX /= d;
        currDirY /= d;

        cursorDots.style.left = currX + 'px';
        cursorDots.style.top = currY + 'px';

        const trailX = -currDirX * spacing;
        const trailY = -currDirY * spacing;
        dots.forEach((dot, i) => {
            const tx = trailX * (i + 1);
            const ty = trailY * (i + 1);
            const lag = 0.28 - i * 0.018;
            dotX[i] += (tx - dotX[i]) * Math.max(lag, 0.06);
            dotY[i] += (ty - dotY[i]) * Math.max(lag, 0.06);
            dot.style.left = dotX[i] + 'px';
            dot.style.top = dotY[i] + 'px';
        });
        requestAnimationFrame(animate);
    }
    animate();
})();
