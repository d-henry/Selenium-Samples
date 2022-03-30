package src.tests;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.junit.jupiter.api.*;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.concurrent.TimeUnit;


public class GoogleSearch {

    private WebDriver driver;

    @BeforeEach
    public void setDriver() {

        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        driver.get("https://google.com");
    }

    @AfterEach
    public void tearDown() throws Exception {
        driver.quit();

    }

    @Test
    public void googleTest() {

        // Find the text box for google search
        // This element doesn't get an ID, so we'll have to use something else to find it.
        WebElement search_box = (new WebDriverWait(driver, 10))
                .until(ExpectedConditions.elementToBeClickable(By.className("gLFyf gsfi")));

        // Send it some text, in this case we'll be searching for Selenium Documentation
        search_box.sendKeys("Selenium Documentation");

        // I think we're feeling lucky
        WebElement feeling_lucky = (new WebDriverWait(driver, 10))
                .until(ExpectedConditions.elementToBeClickable(By.id("gbqfbb")));
        feeling_lucky.click();

        // Let's verify that we are at the Selenium Documentation page.
        String current_url = driver.getCurrentUrl();
        String expected_url = "https://www.selenium.dev/documentation/";

    }

}
