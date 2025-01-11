// 后端环境


// 初始化 Cesium Viewe
const viewer = new Cesium.Viewer('cesiumContainer', {
    terrainProvider: Cesium.createWorldTerrain(),
    imageryProvider: new Cesium.TileMapServiceImageryProvider({
        url: Cesium.buildModuleUrl('Assets/Textures/NaturalEarthII')
    })
});
// 加载 CZML 文件
const czmlDataSource = new Cesium.CzmlDataSource();
czmlDataSource.load('satellites.czml').then(function() {
    viewer.dataSources.add(czmlDataSource);
    viewer.zoomTo(czmlDataSource);
}).otherwise(function(error) {
    console.error('Error loading CZML file:', error);
});

// 启用动画控件
viewer.animation.container.style.visibility = 'visible';
viewer.timeline.container.style.visibility = 'visible';

// 设置初始视角
viewer.scene.camera.setView({
    destination: Cesium.Cartesian3.fromDegrees(0, 0, 10000000) // 从赤道上空 10000 公里处查看
});

// 启用动画
viewer.clock.shouldAnimate = true;