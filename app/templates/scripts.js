document.addEventListener('DOMContentLoaded', () => {

  const videoFileInput = document.getElementById('videoFile');
  const videoPlayer = document.getElementById('videoPlayer');
  const subtitlesDisplay = document.getElementById('subtitlesDisplay');
  const subtitleInput = document.getElementById('subtitleInput');
  const addSubtitleBtn = document.getElementById('addSubtitleBtn');
  const searchInput = document.getElementById('searchInput');
  const searchBtn = document.getElementById('searchBtn');

  let subtitles = [];

  videoFileInput.addEventListener('change', handleVideoFile);

  function handleVideoFile() {
    const file = videoFileInput.files[0];
    videoPlayer.src = URL.createObjectURL(file);
  }

  addSubtitleBtn.addEventListener('click', () => {
    const text = subtitleInput.value.trim();
    if (text) {
      const currentTime = videoPlayer.currentTime;
      subtitles.push({ time: currentTime, text });
      updateSubtitlesDisplay();
      subtitleInput.value = '';
    }
  });

  function updateSubtitlesDisplay() {
    subtitlesDisplay.innerHTML = '';
    for (const subtitle of subtitles) {
      subtitlesDisplay.innerHTML += `<p>${formatTime(subtitle.time)}: ${subtitle.text}</p>`;
    }
  }

  function formatTime(time) {
    const minutes = Math.floor(time / 60);
    const seconds = Math.floor(time % 60);
    return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;

  }

  searchBtn.addEventListener('click', () => {
        const searchText = searchInput.value.trim();
        if (searchText !== '') {
            const matchingSubtitles = subtitlesData.filter(subtitle => subtitle.text.toLowerCase().includes(searchText.toLowerCase()));
            updateSubtitlesDisplay(matchingSubtitles);
        }
    });

  function updateSubtitlesDisplay(subtitles = subtitlesData) {
    subtitlesDisplay.innerHTML = '';
    for (const subtitle of subtitles) {
      const subtitleElement = document.createElement('div');
      subtitleElement.innerHTML = `<strong>${formatTime(subtitle.timestamp)}</strong>: ${subtitle.text}`;
      subtitlesDisplay.appendChild(subtitleElement);
        }
    }

});













