<template>
  <div class="home">

    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
              {{ $t('welcomeTitle') }}
            </p>
            <p class="subtitle">
              {{ $t('welcomeSubtitle') }}
            </p>
        </div>
    </section>
    
  </div>

  <div class="content">

    <img src="../../assets/logo.png" alt="logo">

  </div>

<div class="fixed-grid has-4-cols">
  <div class="grid">

    <div class="cell">
      <div class="card">
        <div class="card-image">
          <figure class="image is-4by3">
            <img
              src="https://bulma.io/assets/images/placeholders/1280x960.png"
              alt="Placeholder image"
            />
          </figure>
        </div>
        <div class="card-content">
          <div class="media">
            <div class="media-content">
              <p class="title is-4">Measure sounds </p>
              <p class="subtitle is-6">with the online soundmeter</p>
            </div>
          </div>

          <div class="content">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec
            iaculis mauris.
            <br />
            
          </div>
        </div>
      </div>
    </div>

    <div class="cell">
      <div class="card">
        <div class="card-image">
          <figure class="image is-4by3">
            <img
              src="https://bulma.io/assets/images/placeholders/1280x960.png"
              alt="Placeholder image"
            />
          </figure>
        </div>
        <div class="card-content">
          <div class="media">
            <div class="media-content">
              <p class="title is-4">See the sounds of everyone</p>
              <p class="subtitle is-6">with the sound map</p>
            </div>
          </div>

          <div class="content">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec
            iaculis mauris.
            <br />
          </div>
        </div>
      </div>
    </div>

    <div class="cell">
      <div class="card">
        <div class="card-image">
          <figure class="image is-4by3">
            <img
              src="https://bulma.io/assets/images/placeholders/1280x960.png"
              alt="Placeholder image"
            />
          </figure>
        </div>
        <div class="card-content">
          <div class="media">
            <div class="media-content">
              <p class="title is-4">See the news about sound</p>
              <p class="subtitle is-6">with the sound news</p>
            </div>
          </div>

          <div class="content">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec
            iaculis mauris.
            <br />
          </div>
        </div>
      </div>
    </div>


    <div class="cell">
      <div class="card">
        <div class="card-image">
          <figure class="image is-4by3">
            <img
              src="https://bulma.io/assets/images/placeholders/1280x960.png"
              alt="Placeholder image"
            />
          </figure>
        </div>
        <div class="card-content">
          <div class="media">
            <div class="media-content">
              <p class="title is-4">Electronic Soundmeter</p>
              <p class="subtitle is-6">check the documentation</p>
            </div>
          </div>

          <div class="content">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec
            iaculis mauris.
            <br />
          </div>
        </div>
      </div>
    </div>

  </div>
</div>


</template>

<script>


export default {
  name: 'HomeView',
  components: {
  }
}
</script>
