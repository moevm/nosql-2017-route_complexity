ymaps.ready(function(){
  var myMap, currentRoute, routePanel;

  myMap = new ymaps.Map("map", {
      center: [59.93, 30.26],
      zoom: 10
  });

  myMap.controls
    .add('routeButtonControl', {
      size: "large",
      float: "right",
      floatIndex: 1000,
    })
    .remove('typeSelector')
    .remove('trafficControl')
    .remove('rulerControl')
    .remove('searchControl');
  myMap.controls.get('routeButtonControl').state.set({
    expanded: 'true'
  });
  myMap.controls.get('routeButtonControl').routePanel.options.set({
    maxWidth: '250px'
  });

  myMap.setType('yandex#map');

//  createRoute("Санкт-петербург, Новоизмайловский проспект, 16 к4", "Санкт-петербург, улица Профессора Попова, 5");

  function createRoute(pointA, pointB) {    // pointA, pointB - точки мультимаршрута.
    // очищаем маршрут
    clearRoute();
          /**
           * Создаем мультимаршрут.
           * @see https://api.yandex.ru/maps/doc/jsapi/2.1/ref/reference/multiRouter.MultiRoute.xml
           */
          currentRoute = new ymaps.multiRouter.MultiRoute({
              referencePoints: [
                  pointA,
                  pointB
              ],
              params: {
                  //Тип маршрутизации - пешеходная маршрутизация.
                  routingMode: 'pedestrian'
              }
          }, {
              // Автоматически устанавливать границы карты так, чтобы маршрут был виден целиком.
              boundsAutoApply: true
          });

      // Добавляем мультимаршрут на карту.
      myMap.geoObjects.add(currentRoute);
  }

  function clearRoute () {
    myMap.geoObjects.remove(currentRoute);
    currentRoute = null;
  }
});
