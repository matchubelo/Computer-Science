package Java;

public class BoilingPoint 
{
    private double temperature; // Fahrenheit

    // Constants for substance freezing/boiling points (F)
    private double ETHYL_FREEZE = -173;
    private double ETHYL_BOIL = 172;
    private double OXY_FREEZE = -362;
    private double OXY_BOIL = -306;
    private double WATER_FREEZE = 32;
    private double WATER_BOIL = 212;

    public BoilingPoint() {
        this.temperature = 0.0;
    }

    public BoilingPoint(double temperature) {
        this.temperature = temperature;
    }

    public double getTemperature() {
        return temperature;
    }

    public void setTemperature(double temperature) {
        this.temperature = temperature;
    }

    public boolean isEthylFreezing() {
        return temperature <= ETHYL_FREEZE;
    }

    public boolean isEthylBoiling() {
        return temperature >= ETHYL_BOIL;
    }

    public boolean isOxygenFreezing() {
        return temperature <= OXY_FREEZE;
    }

    public boolean isOxygenBoiling() {
        return temperature >= OXY_BOIL;
    }

    public boolean isWaterFreezing() {
        return temperature <= WATER_FREEZE;
    }

    public boolean isWaterBoiling() {
        return temperature >= WATER_BOIL;
    }
}
