var rouletter = {
    // 부여할 숫자 랜덤으로 하기
    random: function () {
        min = Math.ceil(0);
        max = Math.floor(5);
        return Math.floor(Math.random() * (max - min)) + min;
    },
    // start 버튼
    start: function () {
        var btn = document.querySelector('.rouletter-btn');
        var panel = document.querySelector('.rouletter-wacu');

        panel.classList.add('on');
        btn.innerText = 'stop';
    },
    // stop 버튼
    stop: function () {
        var btn = document.querySelector('.rouletter-btn');
        var panel = document.querySelector('.rouletter-wacu');
        // 돌림판 형태가 6개로 분할되어있어 필요한 각도를 array로 만들었다.
        // 후에 length로 for문으로 돌려서 array처리로 변경하면 보다 동적으로 대처할수 있겠다.
        var deg = [60, 120, 180, 240, 300, 360];

        panel.style.transform = 'rotate(' + deg[rouletter.random()] + 'deg)';
        panel.classList.remove('on');
        btn.innerText = 'start';
    }
}

document.addEventListener('click', function (e) {
    var target = e.target
    if (target.tagName === 'BUTTON') {
        target.innerText === 'start'
            ? rouletter.start() : rouletter.stop();
    }
})