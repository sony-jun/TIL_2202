const init = {
  monList: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
  dayList: ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일'],
  today: new Date(),
  monForChange: new Date().getMonth(),
  activeDate: new Date(),
  getFirstDay: (yy, mm) => new Date(yy, mm, 1),
  getLastDay: (yy, mm) => new Date(yy, mm + 1, 0),
  nextMonth: function () {
    let d = new Date();
    d.setDate(1);
    d.setMonth(++this.monForChange);
    this.activeDate = d;
    return d;
  },
  prevMonth: function () {
    let d = new Date();
    d.setDate(1);
    d.setMonth(--this.monForChange);
    this.activeDate = d;
    return d;
  },
  addZero: (num) => (num < 10) ? '0' + num : num,
  activeDTag: null,
  getIndex: function (node) {
    let index = 0;
    while (node = node.previousElementSibling) {
      index++;
    }
    return index;
}
};

const $calBody = document.querySelector('.cal-body');
const $btnNext = document.querySelector('.btn-cal.next');
const $btnPrev = document.querySelector('.btn-cal.prev');

function loadYYMM (fullDate) {
  let yy = fullDate.getFullYear();
  let mm = fullDate.getMonth();
  let firstDay = init.getFirstDay(yy, mm);
  let lastDay = init.getLastDay(yy, mm);
  let markToday;  // for marking today date

  if (mm === init.today.getMonth() && yy === init.today.getFullYear()) {
    markToday = init.today.getDate();
}

document.querySelector('.cal-month').textContent = init.monList[mm];
document.querySelector('.cal-year').textContent = yy + '년';

// 날짜가 추가되는 거
let trtd = '';
let startCount;
let countDay = 0;
for (let i = 0; i < 6; i++) {
  trtd += '<tr>';
  for (let j = 0; j < 7; j++) {
    if (i === 0 && !startCount && j === firstDay.getDay()) {
      startCount = 1;
    }
    if (!startCount) {
      trtd += '<td>'
    } else {
      let fullDate = yy + '.' + init.addZero(mm + 1) + '.' + init.addZero(countDay + 1);
      trtd += '<td class="day';
      trtd += (markToday && markToday === countDay + 1) ? ' today" ' : '"';
      trtd += ` data-date="${countDay + 1}" data-fdate="${fullDate}"`;
      let tempDate = yy + '-' + init.addZero(mm + 1) + '-' + init.addZero(countDay + 1);
      trtd += `id="${tempDate}"`;
      trtd += `name="${countDay + 1}">`
    }
    trtd += (startCount) ? ++countDay : '';
    if (countDay === lastDay.getDate()) { 
      startCount = 0; 
    }
    trtd += '</td>';
  }
  trtd += '</tr>';
}
$calBody.innerHTML = trtd;
}

function createNewList (val) {
  let id = new Date().getTime() + '';
  let yy = init.activeDate.getFullYear();
  let mm = init.activeDate.getMonth() + 1;
  let dd = init.activeDate.getDate();
  const $target = $calBody.querySelector(`.day[data-date="${dd}"]`);

  let date = yy + '.' + init.addZero(mm) + '.' + init.addZero(dd);

  let eventData = {};
  eventData['date'] = date;
  eventData['memo'] = val;
  eventData['complete'] = false;
  eventData['id'] = id;
  init.event.push(eventData);
  $todoList.appendChild(createLi(id, val, date));
}

loadYYMM(init.today);

document.querySelector('.cal-day').textContent = '내가 쓴 음악일기 보러가기';
document.querySelector('.cal-date').textContent = '보고싶은 일자를 클릭해주세요';

$btnNext.addEventListener('click', () => loadYYMM(init.nextMonth()));
$btnPrev.addEventListener('click', () => loadYYMM(init.prevMonth()));

$calBody.addEventListener('click', (e) => {
if (e.target.classList.contains('day')) {
  if (init.activeDTag) {
    init.activeDTag.classList.remove('day-active');
    // 각 day 별 id값 접근
    target_id = e.target.getAttribute('id')
    axios({
        method: 'post',
        url: '/articles/id-sort/',
        headers : {'X-CSRFTOKEN' : '{{ csrf_token }}'},
        data: {'target_id': target_id}
      }).then(response => {
        if (response.data.results === 0) {
          document.querySelector('.cal-date').textContent = '작성한 일기가 없습니다.';
        } else{
          document.querySelector('.cal-date').innerHTML = `<a class="show-detail" href="calendar-detail/${target_id}/">작성한 일기 보러가기</a>`;
        }
      })
  }
  let day = Number(e.target.textContent);
  e.target.classList.add('day-active');
  init.activeDTag = e.target;
  init.activeDate.setDate(day);
}
});