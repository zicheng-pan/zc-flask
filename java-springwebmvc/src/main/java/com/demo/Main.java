package com.demo;

import org.apache.catalina.Context;
import org.apache.catalina.LifecycleListener;
import org.apache.catalina.startup.Tomcat;

public class Main {
    public static void main(String[] args) throws Exception {
        Tomcat tomcat = new Tomcat();
        tomcat.setPort(8080);
        // 这里需要指定一个文件路径，不过没什么用，所以我放一个"java.io.tmpdir"临时目录
//        Context context = tomcat.addContext("/", System.getProperty("java.io.tmpdir"));
        Context context = tomcat.addContext("/", System.getProperty("java.io.tmpdir"));
        context.addLifecycleListener((LifecycleListener) Class.forName(tomcat.getHost().getConfigClass()).newInstance());

        tomcat.start();

        tomcat.getServer().await();
    }
}
