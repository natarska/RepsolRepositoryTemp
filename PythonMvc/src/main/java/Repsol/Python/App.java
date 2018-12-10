package Repsol.Python;

import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.logging.LogType;
import org.openqa.selenium.logging.LoggingPreferences;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;

import com.google.j2objc.annotations.ReflectionSupport.Level;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
        
        // capability of chrome obsoleto 
        //DesiredCapabilities cap = DesiredCapabilities.chrome();
        
        //Chrome options instead para establecer chrome driver
        ChromeOptions option = new ChromeOptions();

        
        //
        System.setProperty("webdriver.chrome.driver", "C:\\chromedriver.exe");
        System.setProperty("webdriver.chrome.verboseLogging", "true");
        // Diseño del perfil e inyeccion en el driver
        String chromeProfile = "C:\\Users\\NDiaz\\AppData\\Local\\Google\\Chrome\\User Data";
        option.addArguments("user-data-dir="+chromeProfile);
        option.addArguments("--verbose");
        option.addArguments("--log-path=C:\\chromedriver.log");
        option.addArguments("--start-maximized");
        // With desired capability
        DesiredCapabilities capabilities = DesiredCapabilities.chrome();
        capabilities.setCapability(ChromeOptions.CAPABILITY, option);
       
        // Ejecucion del programa
        WebDriver wd =new ChromeDriver(option);
        String baseUrl = "https://app.powerbi.com/groups/me/apps/b29a0ea9-dd6d-433a-a415-bc3fecd96db8/reports/788dbea5-e2be-4b69-82a0-eec132bdb2f6/";
        wd.get(baseUrl);
        wd.close();
        
        //Ejecucion del script
        String scriptToExecute = "var performance = window.performance || window.mozPerformance "
        		+ "|| window.msPerformance || window.webkitPerformance ||"
        		+ " {}; var network = performance.getEntries() || {}; return network;";
        
        String netData = ((JavascriptExecutor)wd).executeScript(scriptToExecute).toString();
        System.out.println(netData);
        
        FileWriter fo = null;
        try{
        	fo = new FileWriter(new File("C:/logs.txt"));
        	fo.write(netData);
        	fo.close();
        	System.out.println("Final de escritura");
        } catch (Exception e) {
        	System.out.println("ERROR DE ARCHIVO");
        }
    }
}
