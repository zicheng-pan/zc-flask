package com.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@Controller
public class HelloController {
    @RequestMapping("/hello")
    public String sayHello(HttpServletRequest request,
                           HttpServletResponse response,
                           HttpSession session) {
        System.out.println("sayHello");
        System.out.println(request);
        System.out.println(response);
        System.out.println(session);
        return "success11";
    }
}