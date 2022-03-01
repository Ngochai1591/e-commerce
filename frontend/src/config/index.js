const hostName = 'localhost:8000'

const Config = {
    versionAPIProduction: "v1",
    versionAPIDevelopment: "v1",
  
  
    hostProduction: '',
    hostDevelopement: hostName + versionAPIDevelopment,
    language: "en",
    formatDateTime: "YYYY-MM-DD HH:mm:ss",
    formatDateView: "MMMM Do,YYYY",

}

export default Config
