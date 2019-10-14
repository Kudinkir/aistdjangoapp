const ACCESS_TOKEN = '1728285624.cd0a0b8.da60d5a6d13844bc9d74aa11b93223c4';
const COUNT = 8;

export default class Photos {
    constructor(context) {
        this.photos = context.querySelectorAll('.instagram__grid div');
        this.getPhotos();
    }

    getPhotos() {
        fetch(`https://api.instagram.com/v1/users/self/media/recent/?access_token=${ACCESS_TOKEN}&count=${COUNT}`)
            .then(resp => resp.json())
            .then(resp => resp.data.forEach((item, index) => {
                this.photos[index].style.backgroundImage = `url("${item.images.standard_resolution.url}")`
            }))
    }
}