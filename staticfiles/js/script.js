
    let cards = document.querySelectorAll('.card-btn');

    [...cards].forEach((card) => {
      card.addEventListener('click', () => {
        document.querySelector(`.vid${card.dataset.id}`).classList.remove('hide-video');
      });
    });

    let blockers = document.querySelectorAll('.blocker');
    [...blockers].forEach((blocker) => {
      blocker.addEventListener('click', () => {
        document.querySelector(`.vid${blocker.dataset.id}`).classList.add('hide-video');
        let video = document.querySelector(`.video${blocker.dataset.id}`);
        video.currentTime = 0;
        video.pause();
      })
    });


    function playCard(vid_id) {
      let video = document.querySelector(`.video${vid_id}`);
      let mp4 = document.getElementById(`mp4_${vid_id}`)
      let butt = document.getElementById(`myButton${vid_id}`);
      console.log(butt.dataset.dist)
      mp4.src = `https://whereitallbegins.aiesec.org.eg/assets/images/whyEgyptHero/videos/${butt.dataset.dist}.m4v`;
      console.log(mp4.src)
      butt.style.display = "none";
      video.controls = true;
      video.load();
      video.play();
    }
