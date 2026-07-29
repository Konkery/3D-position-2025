ConnectDB =  ConnectDB('rpi03.lan') # выполнить подключение к базе данных Redis


'''
        Не системная функция, выполняет синхронизацию данных между БД и переменными блокнота.  
'''
def AsyncReadDataDB() -> None:
        # Считать массив "сырых" данных из БД
        ImuListRawKey = ('AccArrRaw', 'GyroArrRaw', 'MagArrRaw')
        ImuListRawData = [AccArrRaw, GyroArrRaw, MagArrRaw]
        ReadValJSONfromDB( ConnectDB, ImuListRawKey, ImuListRawData )

        # Считать массив  усредненных данных из БД
        ImuListAvgKey = ('AccArrAvg', 'GyroArrAvg', 'MagArrAvg')
        ImuListAvgData = [AccArrAvg, GyroArrAvg, MagArrAvg]
        ReadValJSONfromDB( ConnectDB, ImuListAvgKey, ImuListAvgData )

        # Считать массивы со значениями углов Эйлера из БД
        AngelListKey = ('AccArrAngle', 'GyroArrAngle', 'CompArrAngle')
        AngelListData = [AccArrAngle, GyroArrAngle, CompArrAngle]
        ReadValJSONfromDB( ConnectDB, AngelListKey, AngelListData )

        # Считать массив со значениями температуры IMU из БД
        TempListKey = ('TempArr',)
        TempListData = [TempArr]
        ReadValJSONfromDB( ConnectDB, TempListKey, TempListData )   

        # Считать значение дельты времени обращений к IMU из БД
        TimeDeltaAngleKey = ('TimeDeltaAngle',)
        TimeDeltaAngleData = [TimeDeltaAngle]
        ReadValJSONfromDB( ConnectDB, TimeDeltaAngleKey, TimeDeltaAngleData )

        # Считать значение коэффициента Альфа, используемого при вычисления значений углов Эйлера в фильтре слияния
        AlphaKey = ('AlphaKey',)
        AlphaData = [Alpha]
        ReadValJSONfromDB( ConnectDB, AlphaKey, AlphaData )