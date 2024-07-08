import { createI18n } from 'vue-i18n';

const messages = {
    'en': {
        soundwave: 'Soundwave : The Earth\'s Ear',
        welcomeTitle: 'Welcome to Soundwave !',
        welcomeSubtitle: 'The Progressive Web App made to measure noise pollution and raise awareness of its negatives effects',
        language: 'Language',
        themeLight: 'Light Theme',
        themeDark: 'Dark Theme',
        accountButton: 'Account',
        loginButton: 'Login',
        soundNews: 'Soundnews',
        soundMeter: 'Soundmeter',
        soundMap: 'Soundmap',
        more: 'See more',

    },
    'fr': {
        soundwave: 'Soundwave : L\'Oreille de la Terre',
        welcomeTitle: 'Bienvenue sur Soundwave !',
        welcomeSubtitle: 'La Progressive Web App faite pour mesurer la pollution sonore et sensibiliser à ses effets négatifs',
        language: 'Langue',
        themeLight: 'Thème lumineux',
        themeDark: 'Thème sombre',
        accountButton: 'Compte',
        loginButton: 'Connexion',
        soundNews: 'Soundnews',
        soundMeter: 'Sonomètre',
        soundMap: 'Carte sonore',
        more: 'Voir plus',
    },
    'de': {
        soundwave: 'Soundwave : Das Ohr Der Erde',
        welcomeTitle: 'Wilkommen bei Soundwave !',
        welcomeSubtitle: 'Eine Progressive Web App gemacht, um die Lärmbelästigung zu messen und sie gegen ihre negativen Folgen zu sensibilisieren',
        language: 'Sprache', 
        themeLight: 'Leuchtendes Thema',
        themeDark: 'Dunkles Thema',
        accountButton: 'Account',
        loginButton: 'Verbinden',
        soundNews: 'Soundnews',
        soundMeter: 'Schallpegelmesser',
        soundMap: 'Soundkarte',
        more: 'Mehr sehen',
    },
    'nl': {
        soundwave: 'Soundwave : Het Oor Van De Aarde',
        welcomeTitle: 'Welkom bij Soundwave !',
        welcomeSubtitle: 'Een Progressive Web App gemaakt om de geluidsoverlast te meten en te sensibiliseren tegen zijn negatieve gevolgen',
        language: 'Taal',
        themeLight: 'Light Theme',
        themeDark: 'Dark Theme',
        accountButton: 'Account',
        loginButton: 'Aansluiting',
        soundNews: 'Soundnews',
        soundMeter: 'Geluidsmeter',
        soundMap: 'Geluidskaart',
        more: 'Bekijk meer',
    },
}

// eslint-disable-next-line
const i18n =  createI18n({
    locale: 'en', // set locale
    fallbackLocale: 'fr', // set fallback locale
    messages, // set locale messages
});

export default i18n;