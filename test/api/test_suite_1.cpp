#include <gtest/gtest.h>

#include "api.hpp"

TEST(TestSomeFunc, ReturnsProperValue) {
    
    int x = 1;
    int result = api::some_func(x);

    EXPECT_EQ(result, 2);
}