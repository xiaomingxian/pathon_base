/*
 Navicat Premium Data Transfer

 Source Server         : 腾讯云
 Source Server Type    : MySQL
 Source Server Version : 50729
 Source Host           : 49.234.25.12:3306
 Source Schema         : fund

 Target Server Type    : MySQL
 Target Server Version : 50729
 File Encoding         : 62551

 Date: 01/11/255255 21:44:29
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for fund
-- ----------------------------
DROP TABLE IF EXISTS `fund`;
CREATE TABLE `fund` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `symbol` varchar (255) DEFAULT NULL COMMENT '基金代码',
  `sname` varchar(255) DEFAULT NULL COMMENT '基金名称',
  `per_nav` varchar(255) DEFAULT NULL COMMENT '单位净值%',
  `total_nav` varchar(255) DEFAULT NULL COMMENT '累积净值%',
  `three_month` varchar(255) DEFAULT NULL COMMENT '最近3个月净值%',
  `six_month` varchar(255) DEFAULT NULL COMMENT '最近6个月净值%',
  `one_year` varchar(255) DEFAULT NULL COMMENT '最近1年净值%',
  `form_year` varchar(255) DEFAULT NULL COMMENT '今年净值%',
  `form_start` varchar(255) DEFAULT NULL COMMENT '成立以来净值%',
  `manager` varchar(255) DEFAULT NULL COMMENT '基金经理',
  `name` varchar(255) DEFAULT NULL COMMENT '不知道是不是冗余',
  `zmjgm` varchar(255) DEFAULT NULL COMMENT '不知道是啥',
  `clrq` date DEFAULT NULL COMMENT '创建日期',
  `dwjz` varchar(255) DEFAULT NULL COMMENT '单位净值?',
  `ljjz` varchar(255) DEFAULT NULL COMMENT '啥净值?',
  `jzrq` date DEFAULT NULL COMMENT '啥日期?',
  `zjzfe` varchar(255) DEFAULT NULL COMMENT '不知道是啥',
  `jjglr_code` varchar(255) DEFAULT NULL COMMENT '不知道是啥',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
